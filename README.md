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
* 실제 빌드/실행 검증과 Launch Parameter 전달은 다음 학습에서 진행

📘 [Notion 상세 정리 - Day 6](https://app.notion.com/p/3dc31ceb5dee815a9275d18927842e00?pvs=204)

---

# 현재 패키지 구조

```text
src/my_pubsub/
├── launch/
│   └── pubsub.launch.py
├── package.xml
├── setup.py
├── setup.cfg
└── my_pubsub/
    ├── __init__.py
    ├── publisher.py
    ├── subscriber.py
    ├── service_server.py
    ├── service_client.py
    ├── action_server.py
    └── action_client.py
```

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

다음 학습:

* [ ] Launch 실행 검증 / Parameter / Remapping / Argument
* [ ] QoS
* [ ] Executor / Callback Group / MultiThread
* [ ] Custom Interface (`.msg`, `.srv`, `.action`)
* [ ] TF2
* [ ] Sensor / Robot Data
* [ ] URDF / RViz / Gazebo
* [ ] Navigation / Manipulation

---

## Build

```bash
cd ~/ros2_ws
colcon build --packages-select my_pubsub
source install/setup.bash
```

## Repository 목적

**ROS 2의 각 기능을 작은 코드로 직접 구현하면서 원리를 이해하고, 이후 AMR 및 실제 로봇 개발에 적용하기 위한 학습 기록**
