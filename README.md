# ROS2 Practice

ROS 2의 기본 개념을 단순히 따라 치는 방식이 아니라, **직접 Node를 구현하고 통신 구조를 확인하면서 원리를 이해하기 위한 학습 저장소**입니다.

현재는 Python(`rclpy`)을 이용해 ROS 2의 핵심 통신 방식인 Topic, Parameter, Service, Action을 단계적으로 실습하고 있습니다.

## 학습 목표

- ROS 2의 Node와 통신 구조를 이해한다.
- Publisher / Subscriber를 직접 구현한다.
- Parameter를 이용해 실행 시 설정값을 변경하는 방법을 익힌다.
- Service의 Request / Response 구조와 Client / Server의 역할을 이해한다.
- Action의 Goal / Feedback / Result 구조를 이해한다.
- 이후 Launch, QoS, Interface, TF2, Navigation 등 실제 로봇 개발에 필요한 개념으로 확장한다.

## 실습 환경

- Windows
- WSL2 Ubuntu 22.04
- Docker Desktop
- ROS 2 Humble
- Python 3.10
- VS Code
- ROS 2 Workspace: `~/ros2_ws`

---

# Day 1 - 실습 환경 구축 및 Node / Topic 기초

## 목적

ROS 2 프로그램이 어떤 단위로 실행되고, Node들이 Topic을 통해 어떻게 데이터를 주고받는지 이해하는 것이 목표입니다.

## 학습 내용

- WSL2 + Docker 기반 ROS 2 Humble 실습 환경 구성
- ROS 2 환경 source 개념
- `ros2` CLI 기본 사용법
- Node 개념
- Topic 개념
- Message 개념
- Publisher / Subscriber 역할
- `turtlesim`을 이용한 Node / Topic 확인
- ROS 2의 DDS 기반 Dynamic Discovery 개념 확인

## 핵심 정리

```text
Node
 ├─ Publisher ── Topic ──> Subscriber
 └─ Subscriber <─ Topic ── Publisher
```

ROS 2에서는 각 Node가 독립적으로 실행되며, DDS를 통해 서로를 발견하고 통신합니다.

---

# Day 2 - Python Publisher / Subscriber 패키지 실습

## 목적

CLI로 ROS 2를 관찰하는 단계에서 벗어나, Python 코드로 직접 Node를 만들어 ROS 2 통신 구조를 구현하는 것이 목표입니다.

## 학습 내용

- ROS 2 Workspace 구조 이해
  - `src`
  - `build`
  - `install`
  - `log`
- `ament_python` 패키지 구조 이해
- `package.xml` 의존성 관리
- `setup.py`의 `console_scripts` 등록
- Python Publisher Node 구현
- Python Subscriber Node 구현
- `std_msgs/msg/String` 사용
- Timer callback 구현
- Subscriber callback 구현
- `colcon build` 사용
- `ros2 run`으로 직접 만든 Node 실행
- `ros2 node list`, `ros2 topic list`, `ros2 topic echo` 등을 이용한 통신 확인

## 구현 구조

```text
my_publisher
     │
     │  std_msgs/String
     ▼
  /chatter
     │
     ▼
my_subscriber
```

Publisher가 주기적으로 메시지를 보내고 Subscriber가 Topic을 통해 해당 메시지를 수신하도록 구현했습니다.

---

# Day 3 - Parameter / Service / Action 기초

## 목적

Publisher / Subscriber를 넘어 ROS 2에서 설정값을 관리하고, 요청-응답 통신과 장시간 작업을 처리하는 방법을 이해하는 것이 목표입니다.

## 1. Parameter

Publisher의 timer 주기를 하드코딩하지 않고 Parameter로 관리하도록 변경했습니다.

```python
self.declare_parameter('timer_period', 1.0)
timer_period = self.get_parameter('timer_period').value
```

실행 시 Parameter를 변경할 수 있습니다.

```bash
ros2 run my_pubsub publisher --ros-args -p timer_period:=0.2
```

### 배운 점

- Parameter 선언: `declare_parameter()`
- Parameter 조회: `get_parameter()`
- CLI Parameter 확인
  - `ros2 param list`
  - `ros2 param get`
  - `ros2 param set`
- Parameter 값이 변경되어도 이미 생성된 Timer가 자동으로 다시 생성되는 것은 아니라는 점 확인

---

## 2. Service

`example_interfaces/srv/AddTwoInts`를 사용해 Service Server와 Client를 구현했습니다.

### 구조

```text
Service Client
      │
      │ Request (a, b)
      ▼
/add_two_ints
      │
      ▼
Service Server
      │
      │ Response (sum)
      ▼
Service Client
```

### 학습 내용

- `create_service()`
- Service callback
- `create_client()`
- `wait_for_service()`
- `call_async()`
- Future 객체
- `spin_until_future_complete()`
- Request / Response 구조
- 하나의 Node가 여러 Service 또는 여러 Client를 가질 수 있다는 점 확인

### Service와 Topic의 차이

```text
Topic   : 지속적으로 데이터를 전달
Service : 요청 1회 -> 응답 1회
```

---

## 3. Action

오래 걸리는 작업을 처리하기 위한 ROS 2 Action의 기본 구조를 학습했습니다.

`example_interfaces/action/Fibonacci`를 사용해 Action Server를 구현하고 CLI를 Action Client처럼 사용해 테스트했습니다.

### Action 핵심 구조

```text
Action Client
      │
      │ Goal
      ▼
Action Server
      │
      ├── Feedback
      ├── Feedback
      ├── Feedback
      │
      └── Result
```

### 핵심 개념

- Goal: 수행할 목표
- Feedback: 작업 중간 진행 상태
- Result: 최종 결과
- Cancel: 진행 중인 Goal 취소
- `ActionServer`
- `execute_callback()`
- `goal_handle`
- `goal_handle.request`
- `goal_handle.publish_feedback()`
- `goal_handle.succeed()`

CLI를 이용해 Goal을 전달하고 Feedback과 Result가 순서대로 오는 것을 직접 확인했습니다.

```bash
ros2 action send_goal /fibonacci example_interfaces/action/Fibonacci "{order: 5}" --feedback
```

---

# 현재 패키지 구조

```text
src/my_pubsub/
├── package.xml
├── setup.py
├── setup.cfg
└── my_pubsub/
    ├── __init__.py
    ├── publisher.py
    ├── subscriber.py
    ├── service_server.py
    ├── service_client.py
    └── action_server.py
```

---

# 학습 진행 방향

현재까지:

- [x] Node / Topic / Message
- [x] Publisher / Subscriber
- [x] ROS 2 Python Package
- [x] Parameter
- [x] Service
- [x] Action Server / Goal / Feedback / Result 기초

다음 학습:

- [ ] Action Client
- [ ] Action Cancel / 상태 처리
- [ ] Launch
- [ ] QoS
- [ ] Custom Interface (`.msg`, `.srv`, `.action`)
- [ ] TF2
- [ ] Sensor / Robot Data
- [ ] URDF / RViz / Gazebo
- [ ] Navigation / Manipulation

---

## Build

```bash
cd ~/ros2_ws
colcon build --packages-select my_pubsub
source install/setup.bash
```

## Repository 목적

이 저장소는 완성된 ROS 2 프로젝트보다는 **ROS 2의 각 기능을 작은 코드로 직접 구현하면서 원리를 이해하고, 이후 AMR 및 실제 로봇 개발에 적용하기 위한 학습 기록**을 목적으로 합니다.
