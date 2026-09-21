# ROS2 Practice

## 학습 목표

* ROS 2의 Node와 통신 구조 이해
* Publisher / Subscriber 구현
* Parameter를 이용해 실행 시 설정값을 변경하는 방법 학습
* Service의 Request / Response 구조와 Client / Server의 역할 이해
* Action의 Goal / Feedback / Result / Cancel 구조 이해
* 이후 Launch, QoS, Executor, Interface, TF2, Navigation 등 실제 로봇 개발에 필요한 개념으로 확장

## 실습 환경

* Windows
* WSL2 Ubuntu 22.04
* Docker Desktop
* ROS 2 Humble
* Python 3.10
* VS Code
* ROS 2 Workspace: `~/ros2_ws`

---

# 학습 기록

## Day 1 - 실습 환경 구축 및 Node / Topic 기초

**목적:** ROS 2의 실행 단위인 Node와 Topic 기반 통신 구조 이해

* WSL2 + Docker + ROS 2 Humble 실습 환경 구성
* Node / Topic / Message / Publisher / Subscriber 기초
* `turtlesim`, ROS 2 CLI, DDS Discovery 확인

📘 [Notion 상세 정리 - Day 1](https://app.notion.com/p/3d031ceb5dee80ebaf2cdd0a9dcafff4?pvs=204)

---

## Day 2 - Python Publisher / Subscriber 패키지 실습

**목적:** Python으로 직접 ROS 2 Node와 Topic 통신 구현

* Workspace / `ament_python` 패키지 구조
* Publisher / Subscriber 구현
* Timer / Subscriber callback
* `colcon build`, `ros2 run` 및 CLI 확인

📘 [Notion 상세 정리 - Day 2](https://app.notion.com/p/3d131ceb5dee819898cce70793de3f45?pvs=204)

---

## Day 3 - Parameter / Service / Action 기초

**목적:** 설정 관리, 요청-응답 통신, 장시간 작업 처리 방식 이해

* Parameter 선언 / 조회 / 실행 시 override
* Service Server / Client, Request / Response, Future
* Action Server, Goal / Feedback / Result, `goal_handle`

📘 [Notion 상세 정리 - Day 3](https://app.notion.com/p/3d431ceb5dee8193a517f944a88cba3f?pvs=204)

---

## Day 4 - Action Client / GoalHandle / Future 심화

**목적:** Action Client의 비동기 통신 구조와 Goal 생명주기 이해

* Action Client 구현 및 Goal / Feedback / Result 흐름 확인
* `ClientGoalHandle` / `ServerGoalHandle` 역할과 내부 구조 비교
* `send_goal_async()` / `get_result_async()`와 Future 관계 이해
* Feedback callback 및 Result callback 처리
* `spin_once()`, `destroy_node()`, `shutdown()`을 통한 Node 생명주기 이해
* `goal_callback`과 Goal ACCEPT / REJECT 구조
* `ActionClient` 객체와 `Node` 상속 / `super().__init__()` 구조 이해

📘 [Notion 상세 정리 - Day 4](https://app.notion.com/p/3d531ceb5dee81a7a190f0f617daec02?pvs=204)

---

## Day 5 - Future 심화 / Action Cancel / 상태 처리

**목적:** Future의 완료 구조와 Action Goal 상태 전이 및 Cancel 처리 흐름 이해

* Future의 `done()`, `result()`, `exception()`, `add_done_callback()` 역할 이해
* Future 상태와 Action Goal 상태의 차이 이해
* Action Goal 상태 전이 이해

  * ACCEPTED
  * EXECUTING
  * CANCELING
  * SUCCEEDED
  * CANCELED
  * ABORTED
* Server의 `cancel_callback()` / `CancelResponse` 구현
* `goal_handle.is_cancel_requested`를 이용한 Cancel 요청 확인
* `goal_handle.canceled()`를 이용한 CANCELED 상태 처리
* Client의 `cancel_goal_async()` 구현
* Cancel Future와 Cancel Response 처리
* `GoalStatus`를 이용한 SUCCEEDED / CANCELED / ABORTED 최종 상태 확인
* Feedback sequence 길이가 5 이상일 때 자동 Cancel하도록 실습
* 실제 Server / Client 실행을 통해 Cancel 동작 확인
* Cancel 처리를 위해 `ReentrantCallbackGroup`, `MultiThreadedExecutor`를 최소 설정으로 사용

📘 [Notion 상세 정리 - Day 5](https://app.notion.com/p/3d631ceb5dee81a19341cfec9007345f?pvs=204)

> `Executor / Callback Group / MultiThread`는 Day 5에서 정식 학습한 것이 아니라 Action Cancel 실습을 동작시키기 위한 최소 설정으로만 사용했다. 해당 내용은 QoS 이후 별도 단원에서 정식으로 학습한다.

---

## Day 6 - Launch 기초 / 여러 Node 동시 실행

**목적:** 여러 ROS 2 Node를 Launch 파일 하나로 관리하는 기본 구조 이해

* Python Launch 파일의 기본 구조 이해
* `launch_ros.actions.Node`와 `rclpy.node.Node`의 차이 이해
* Publisher / Subscriber 동시 실행용 `pubsub.launch.py` 작성
* `setup.py`에 Launch 파일 설치 설정 추가
* `package.xml`에 `launch`, `launch_ros` 실행 의존성 추가
* Launch 파일 빌드 및 실행 검증

📘 [Notion 상세 정리 - Day 6](https://app.notion.com/p/3dc31ceb5dee815a9275d18927842e00?pvs=204)

---

## Day 7 - Launch 심화 / QoS

**목적:** Launch 실행 설정을 확장하고 ROS 2 통신의 QoS 정책과 호환성 이해

### Launch 심화

* Launch에서 Publisher Parameter 전달 및 `timer_period` override
* `name`을 이용한 Node 이름 변경
* `remappings`를 이용한 Topic 이름 변경
* `DeclareLaunchArgument` / `LaunchConfiguration`을 이용한 실행 시 값 전달
* Namespace를 이용한 Node / Topic 그룹 분리
* `robot1`, `robot2` Namespace로 동일 Publisher / Subscriber 구성 동시 실행
* 동일 코드를 재사용하면서 Robot별 Parameter / Topic 분리 확인

### QoS

* 기존 Publisher / Subscriber의 QoS 숫자 `10`을 `QoSProfile`로 명시화
* History / Depth 개념 이해
* `RELIABLE` / `BEST_EFFORT` 차이 및 Requested / Offered 호환성 이해
* `VOLATILE` / `TRANSIENT_LOCAL` 차이 이해
* Publisher / Subscriber 각각의 QoS 설정과 호환성 확인
* Sensor Data QoS와 `qos_profile_sensor_data` 개념 확인
* `ros2 topic info <topic> --verbose`를 통한 실제 QoS 확인 방법 학습

📘 [Notion 상세 정리 - Day 7](https://app.notion.com/p/3dd31ceb5dee81988eadf24fdfdb84b3?pvs=204)

> 다음 학습부터 `Executor / Callback Group / MultiThread`를 정식으로 진행한다.


---

## Day 8 - Executor / Callback Group / MultiThread

**목적:** ROS 2 callback 실행 구조와 MultiThread 환경에서의 동시 실행 조건 이해

* SingleThreadedExecutor에서 긴 callback이 다른 callback 실행을 지연시키는 현상 확인
* MultiThreadedExecutor를 적용해 여러 worker thread를 사용하는 구조 이해
* 기본 `MutuallyExclusiveCallbackGroup`에서는 Thread가 여러 개여도 같은 Group의 callback이 동시에 실행되지 않는 점 확인
* FAST / SLOW Timer를 서로 다른 `MutuallyExclusiveCallbackGroup`으로 분리해 동시 실행 확인
* 하나의 `ReentrantCallbackGroup` 안에서 callback 동시 실행 확인
* Reentrant 사용 시 공유 변수 / 로봇 제어 / Serial / 파일 등 공유 자원 접근 주의점 학습
* 기존 Action Cancel 코드와 `ReentrantCallbackGroup + MultiThreadedExecutor` 구조 연결
* `cancel_callback()`, `is_cancel_requested`, `goal_handle.canceled()` 역할 재정리
* `num_threads=2` / `num_threads=4` 비교 및 `threading.get_ident()`으로 실제 worker thread 확인
* Python GIL과 MultiThreadedExecutor의 관계 이해
* 하나의 Executor가 여러 Node를 `add_node()`로 관리할 수 있는 구조 학습

📘 [Notion 상세 정리 - Day 8](https://app.notion.com/p/3df31ceb5dee81d3a8cee3fc7393939b?pvs=204)

> 다음 학습은 하나의 Executor에서 Publisher / Subscriber Node를 함께 실행하는 실습 확인 후 Custom Interface로 진행한다.

---
---

## Day 8 - Executor / Callback Group / MultiThread

**목적:** ROS 2 Callback 실행 구조와 MultiThread 환경에서 Callback의 동시 실행 조건 이해

### Executor

* `rclpy.spin(node)`을 이용한 SingleThreadedExecutor 동작 확인
* 긴 Callback이 실행될 때 다른 Callback의 실행이 지연되는 현상 확인
* `MultiThreadedExecutor`를 이용한 여러 Worker Thread 구조 이해
* `num_threads=2`, `num_threads=4` 비교
* `threading.get_ident()`을 이용해 실제 Callback이 실행되는 Thread 확인
* Thread 개수가 많다고 항상 성능이 좋아지는 것은 아니라는 점 이해
* Python GIL과 MultiThreadedExecutor의 관계 이해

### Callback Group

* 기본 Callback Group이 `MutuallyExclusiveCallbackGroup`이라는 점 확인
* 같은 `MutuallyExclusiveCallbackGroup`의 Callback은 MultiThreadedExecutor에서도 동시에 실행되지 않음
* 서로 다른 `MutuallyExclusiveCallbackGroup`으로 분리하면 동시 실행 가능
* `ReentrantCallbackGroup`을 이용해 같은 Group 내부 Callback의 동시 실행 확인
* 공유 변수, Robot API, Serial, 파일 등 공유 자원에 대한 동시 접근 주의

### Action Cancel과 Executor 연결

* 기존 Action Server의 `ReentrantCallbackGroup` 구조 재확인
* `MultiThreadedExecutor(num_threads=2)`가 필요한 이유 이해
* `cancel_callback()`은 Cancel 요청의 ACCEPT / REJECT를 결정
* `goal_handle.is_cancel_requested`로 실행 중 Cancel 요청 확인
* `goal_handle.canceled()`로 Goal을 최종 CANCELED 상태로 변경
* 긴 `execute_callback()` 실행 중에도 Cancel 요청을 처리할 수 있는 구조 이해

### Multi-node Executor

* 하나의 Executor에 여러 Node를 `add_node()`로 등록할 수 있는 구조 이해
* Publisher / Subscriber를 하나의 Process에서 관리하는 구조 학습
* Node와 Process가 서로 다른 개념이라는 점 이해
* Launch로 여러 Process를 실행하는 방식과 하나의 Executor에서 여러 Node를 실행하는 방식 비교

📘 [Notion 상세 정리 - Day 8](https://app.notion.com/p/3df31ceb5dee81d3a8cee3fc7393939b?pvs=204)

---

## Day 9 - Custom Interface (.msg / .srv / .action)

**목적:** ROS 2에서 프로젝트에 필요한 Message / Service / Action 타입을 직접 정의하고 사용하는 방법 이해

### Interface Package

* Custom Interface 전용 `my_interfaces` 패키지 생성
* Interface 패키지를 `ament_cmake` 방식으로 구성
* `rosidl_default_generators`를 이용한 Interface 코드 생성 구조 이해
* `my_pubsub`와 `my_interfaces` 패키지 역할 분리

### Custom Message

* `RobotStatus.msg` 작성

```text
string robot_name
int32 battery
bool is_moving
```

* `RobotStatus`를 사용하는 Custom Publisher / Subscriber 구현
* `/robot_status` Topic을 통해 Custom Message 통신 확인
* `ros2 interface show`, `ros2 topic type`, `ros2 topic echo`로 Interface 확인

### Custom Service

* `SetTarget.srv` 작성

```text
float64 x
float64 y
---
bool success
string message
```

* `.srv`의 Request / Response 구조 이해
* Custom Service Server / Client 구현
* `/set_target` Service 호출 확인

### Custom Action

* `MoveRobot.action` 작성

```text
float64 x
float64 y
---
bool success
string message
---
float64 progress
```

* `.action`의 Goal / Result / Feedback 구조 이해
* Custom Action Server / Client 구현
* Goal 전달, Feedback 수신, Result 반환 흐름 확인
* `ros2 action send_goal --feedback`을 이용한 CLI 테스트

### Interface 생성 과정

```text
.msg / .srv / .action
        ↓
rosidl_generate_interfaces()
        ↓
colcon build
        ↓
Python / C++ Interface 코드 생성
        ↓
ROS 2 Node에서 사용
```

* `my_pubsub/package.xml`에 `my_interfaces` dependency 추가
* Interface를 사용하는 패키지 간 dependency 관계 이해

### Nested Message / Array / Constant

* `RobotCommand.msg` 작성

```text
uint8 MODE_IDLE=0
uint8 MODE_MOVING=1
uint8 MODE_ERROR=2

string robot_name
geometry_msgs/Pose target_pose
float64 speed
bool enable
float64[6] joint_angles
uint8 mode
```

* Custom Message 안에서 `geometry_msgs/Pose` 같은 기존 ROS Message 사용
* Nested Message 구조 이해
* 가변 길이 배열 `[]` 문법 이해
* 고정 길이 배열 `[6]` 문법 이해
* Message 상수 정의 및 사용 방법 학습
* `geometry_msgs` dependency 추가 방법 학습

📘 [Notion 상세 정리 - Day 9](https://app.notion.com/p/3e231ceb5dee812a928dc2abc57ba0a5?pvs=204)

> 다음 학습에서는 `RobotCommand`를 실제 Publisher에서 사용해 `Pose`, 배열, 상수 값을 전송한 뒤 Custom Interface 단원을 마무리하고 TF2로 진행한다.

---

# 학습 진행 방향

현재까지:

* [x] Node / Topic / Message
* [x] Publisher / Subscriber
* [x] ROS 2 Python Package
* [x] Parameter
* [x] Service
* [x] Action Server / Goal / Feedback / Result 기초
* [x] Action Client / GoalHandle / Future
* [x] Goal ACCEPT / REJECT
* [x] Action Cancel / 상태 처리
* [x] Launch 기초 및 Launch 파일 작성
* [x] Launch 실행 검증 / Parameter / Remapping / Argument / Namespace
* [x] QoS
* [x] Executor / Callback Group / MultiThread
* [x] Custom Interface (`.msg`, `.srv`, `.action`)

다음 학습:

* [ ] TF2
* [ ] Sensor / Robot Data
* [ ] URDF / RViz / Gazebo
* [ ] SLAM
* [ ] Navigation2
* [ ] 실제 AMR 구조 적용


---

## Build

```bash
cd ~/ros2_ws
colcon build --packages-select my_pubsub
source install/setup.bash
```

## Repository 목적

**ROS 2의 각 기능을 작은 코드로 직접 구현하면서 원리를 이해하고, 이후 AMR 및 실제 로봇 개발에 적용하기 위한 학습 기록**
