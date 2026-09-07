# ROS2 Practice

## 학습 목표

- ROS 2의 Node와 통신 구조 이해
- Publisher / Subscriber 구현
- Parameter를 이용해 실행 시 설정값을 변경하는 방법 학습
- Service의 Request / Response 구조와 Client / Server의 역할 이해
- Action의 Goal / Feedback / Result 구조 이해
- 이후 Launch, QoS, Interface, TF2, Navigation 등 실제 로봇 개발에 필요한 개념으로 확장

## 실습 환경

- Windows
- WSL2 Ubuntu 22.04
- Docker Desktop
- ROS 2 Humble
- Python 3.10
- VS Code
- ROS 2 Workspace: `~/ros2_ws`

---

# 학습 기록

## Day 1 - 실습 환경 구축 및 Node / Topic 기초

**목적:** ROS 2의 실행 단위인 Node와 Topic 기반 통신 구조 이해

- WSL2 + Docker + ROS 2 Humble 실습 환경 구성
- Node / Topic / Message / Publisher / Subscriber 기초
- `turtlesim`, ROS 2 CLI, DDS Discovery 확인

📘 [Notion 상세 정리 - Day 1](https://app.notion.com/p/3d031ceb5dee80ebaf2cdd0a9dcafff4?pvs=204)

---

## Day 2 - Python Publisher / Subscriber 패키지 실습

**목적:** Python으로 직접 ROS 2 Node와 Topic 통신 구현

- Workspace / `ament_python` 패키지 구조
- Publisher / Subscriber 구현
- Timer / Subscriber callback
- `colcon build`, `ros2 run` 및 CLI 확인

📘 [Notion 상세 정리 - Day 2](https://app.notion.com/p/3d131ceb5dee819898cce70793de3f45?pvs=204)

---

## Day 3 - Parameter / Service / Action 기초

**목적:** 설정 관리, 요청-응답 통신, 장시간 작업 처리 방식 이해

- Parameter 선언 / 조회 / 실행 시 override
- Service Server / Client, Request / Response, Future
- Action Server, Goal / Feedback / Result, `goal_handle`

📘 [Notion 상세 정리 - Day 3](https://app.notion.com/p/3d431ceb5dee8193a517f944a88cba3f?pvs=204)

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

**ROS 2의 각 기능을 작은 코드로 직접 구현하면서 원리를 이해하고, 이후 AMR 및 실제 로봇 개발에 적용하기 위한 학습 기록**
