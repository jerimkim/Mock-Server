# 티켓팅 Mock Server

Flask 기반의 티켓팅 시스템 통합 테스트용 Mock Server입니다.

## 서비스 구성

### 1. HKDL (홍콩 디즈니랜드) Mock Server
- **포트**: 5000
- **인증**: SHA-256 서명 기반
- **API 타입**: POST (OTA 엔드포인트)

### 2. Ingresso (Ticketswitch f13 API) Mock Server
- **포트**: 5001
- **인증**: Basic Auth (demo:demopass)
- **API 타입**: GET/POST (RESTful)

## 빠른 시작

### Docker Compose로 실행

```bash
# 서비스 시작
docker-compose up -d

# 로그 확인
docker-compose logs -f

# 서버 상태 확인
curl http://localhost:5000/health
curl http://localhost:5001/health

# 서비스 중지
docker-compose down
```

### 로컬 개발 환경 실행

#### HKDL Server
```bash
cd hkdl
pip install -r requirements.txt
python app.py
```

#### Ingresso Server
```bash
cd ingresso
pip install -r requirements.txt
python app.py
```

## API 엔드포인트

### HKDL (포트 5000)
| 엔드포인트 | 메서드 | 설명 |
|----------|--------|------|
| `/health` | GET | 상태 체크 |
| `/OTA/GetEvents` | POST | 이벤트 목록 조회 |
| `/OTA/GetShows` | POST | 쇼 정보 조회 |
| `/OTA/GetTickets` | POST | 티켓 타입 조회 |
| `/OTA/GetPickupDetails` | POST | 픽업 방법 조회 |
| `/OTA/ReserveOrder` | POST | 티켓 예약 |
| `/OTA/CancelOrder` | POST | 예약 취소 |
| `/OTA/GetOrderStatus` | POST | 주문 상태 조회 |

### Ingresso (포트 5001)
| 엔드포인트 | 메서드 | 설명 |
|----------|--------|------|
| `/health` | GET | 상태 체크 |
| `/f13/events.v1` | GET | 이벤트 목록 조회 |
| `/f13/events_by_id.v1` | GET | 이벤트 상세 조회 |
| `/f13/months.v1` | GET | 이용 가능한 월 조회 |
| `/f13/performances.v1` | GET | 공연 정보 조회 |
| `/f13/performances_by_id.v1` | GET | 공연 상세 조회 |
| `/f13/availability.v1` | GET | 좌석 가용성 조회 |
| `/f13/reserve.v1` | POST | 티켓 예약 |
| `/f13/test_errors.v1` | GET | 에러 응답 테스트 |
| `/f13/test_errors.v1/list` | GET | 테스트 가능한 에러 목록 조회 |

## 에러 응답 테스트 (Ingresso)

Ingresso Mock Server는 다양한 에러 시나리오를 테스트할 수 있는 전용 엔드포인트를 제공합니다.

### 사용 가능한 에러 목록 조회
```bash
# 인증 불필요
curl http://localhost:5001/f13/test_errors.v1/list
```

### 에러 테스트 예시

#### 일반 에러 (error_code: 2-8)
```bash
# Bad channel (error_code: 2)
curl -u demo:demopass "http://localhost:5001/f13/test_errors.v1?error_code=2"

# User authentication failure (error_code: 3)
curl -u demo:demopass "http://localhost:5001/f13/test_errors.v1?error_code=3"

# Backend connection failure (error_code: 4)
curl -u demo:demopass "http://localhost:5001/f13/test_errors.v1?error_code=4"

# Bad data supplied (error_code: 8)
curl -u demo:demopass "http://localhost:5001/f13/test_errors.v1?error_code=8"
```

#### 이메일 에러 (error_code: 2000)
```bash
# 이메일 공백
curl -u demo:demopass "http://localhost:5001/f13/test_errors.v1?error_code=2000&email_error_key=addr_may_not_be_blank"

# @ 기호 누락
curl -u demo:demopass "http://localhost:5001/f13/test_errors.v1?error_code=2000&email_error_key=addr_missing_at"

# 잘못된 도메인
curl -u demo:demopass "http://localhost:5001/f13/test_errors.v1?error_code=2000&email_error_key=addr_bad_email_domain"
```

#### 카드 에러 (error_code: 3000-3008)
```bash
# 인식할 수 없는 카드
curl -u demo:demopass "http://localhost:5001/f13/test_errors.v1?error_code=3000"

# 유효하지 않은 카드 번호
curl -u demo:demopass "http://localhost:5001/f13/test_errors.v1?error_code=3002"

# 유효하지 않은 만료일
curl -u demo:demopass "http://localhost:5001/f13/test_errors.v1?error_code=3003"

# 유효하지 않은 CV2
curl -u demo:demopass "http://localhost:5001/f13/test_errors.v1?error_code=3004"
```

### HTTP 상태 코드 매핑

| error_code | HTTP Status | 설명 |
|-----------|-------------|------|
| 2 | 460 | Invalid Parameters |
| 3 | 401 | Unauthorised |
| 4 | 502 | Bad Gateway |
| 5 | 403 | Forbidden |
| 6 | 500 | Internal Server Error |
| 7 | 401 | Unauthorised |
| 8 | 460 | Invalid Parameters |
| 2000 | 460 | Invalid Parameters (Email) |
| 3000-3008 | 460 | Invalid Parameters (Card) |

## 테스트 방법

### HKDL 테스트
```bash
cd hkdl
python test_api.py all
```

### Ingresso 테스트
```bash
# 상태 체크
curl http://localhost:5001/health

# 이벤트 조회 (Basic Auth 필요)
curl -u demo:demopass "http://localhost:5001/f13/events.v1?keywords=sphere"

# 가용성 조회
curl -u demo:demopass "http://localhost:5001/f13/availability.v1?perf_id=1GNCR-5"

# 공연 조회
curl -u demo:demopass "http://localhost:5001/f13/performances.v1?event_id=1GNC&date=2025-01-20"
```

또는 테스트 스크립트 실행:
```bash
cd ingresso
python test_api.py all
```

## 프로젝트 구조

```
Mock-Server/
├── docker-compose.yml          # Docker Compose 설정
├── .dockerignore              # Docker 제외 파일
├── README.md                   # 현재 문서
│
├── hkdl/                       # HKDL Mock Server
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── app.py                 # Flask 애플리케이션
│   ├── auth.py                # SHA-256 인증
│   ├── config.py              # 설정
│   ├── mock_data.py           # Mock 응답 데이터
│   └── test_api.py            # 테스트 스크립트
│
└── ingresso/                   # Ingresso Mock Server
    ├── Dockerfile
    ├── requirements.txt
    ├── app.py                 # Flask 애플리케이션
    ├── auth.py                # Basic 인증
    ├── config.py              # 설정
    ├── mock_data.py           # Mock 응답 데이터 (40+ 티켓 타입)
    └── test_api.py            # 테스트 스크립트
```

## 환경 설정

### HKDL 환경 변수
```bash
SECRET_AUTHENTICATION_KEY=xY378DS731A
AGENT_ID=MYREALTRIP
```

### Ingresso 환경 변수
```bash
USERNAME=demo
PASSWORD=demopass
```

## Docker 명령어

```bash
# 이미지 빌드
docker-compose build

# 백그라운드로 서비스 시작
docker-compose up -d

# 로그 확인
docker-compose logs -f hkdl
docker-compose logs -f ingresso

# 특정 서비스 재시작
docker-compose restart hkdl
docker-compose restart ingresso

# 모든 서비스 중지
docker-compose down

# 컨테이너 및 볼륨 전체 삭제
docker-compose down -v

# 리소스 사용량 확인
docker stats
```

## 문제 해결

### 포트가 이미 사용 중일 때

```bash
# 포트 사용 프로세스 확인
lsof -i :5000
lsof -i :5001

# 프로세스 종료
kill -9 <PID>

# 또는 docker-compose.yml에서 포트 변경
ports:
  - "5002:5000"  # 다른 호스트 포트 사용
```

### 컨테이너가 시작되지 않을 때

```bash
# 로그 확인
docker-compose logs hkdl
docker-compose logs ingresso

# 컨테이너 상태 확인
docker-compose ps

# 캐시 없이 재빌드
docker-compose build --no-cache
docker-compose up -d
```

### Health Check 실패 시

```bash
# 컨테이너 내부에서 서비스 확인
docker-compose exec hkdl curl http://localhost:5000/health
docker-compose exec ingresso curl http://localhost:5001/health

# 애플리케이션 로그 확인
docker-compose logs -f
```

### Import 에러 발생 시

```bash
# 완전히 재빌드
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

## AWS 배포 가이드

### 방법 1: EC2 + Docker Compose (가장 간단)

#### 1. EC2 인스턴스 생성
- AMI: Amazon Linux 2023 또는 Ubuntu 22.04
- 인스턴스 타입: t3.micro (프리티어) 또는 t3.small
- 보안 그룹: 22, 5000, 5001 포트 허용

#### 2. Docker 설치
```bash
# EC2 접속
ssh -i your-key.pem ec2-user@your-ec2-ip

# Docker 설치
sudo yum update -y
sudo yum install -y docker
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -a -G docker ec2-user

# Docker Compose 설치
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# 재접속 (그룹 권한 적용)
exit
ssh -i your-key.pem ec2-user@your-ec2-ip
```

#### 3. 애플리케이션 배포
```bash
# 코드 업로드 (또는 git clone)
git clone <your-repo-url>
cd Mock-Server

# 서비스 시작
docker-compose up -d

# 확인
docker-compose ps
curl http://localhost:5000/health
curl http://localhost:5001/health
```

#### 4. 외부에서 접속
```bash
# 로컬에서 테스트
curl http://<EC2-PUBLIC-IP>:5000/health
curl http://<EC2-PUBLIC-IP>:5001/health
```

### 방법 2: ECS Fargate (관리형, 서버 유지보수 불필요)

```bash
# ECR 로그인
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com

# 리포지토리 생성
aws ecr create-repository --repository-name hkdl-mock-server
aws ecr create-repository --repository-name ingresso-mock-server

# 이미지 빌드 및 푸시
docker-compose build
docker tag mock-server_hkdl:latest <account-id>.dkr.ecr.us-east-1.amazonaws.com/hkdl-mock-server:latest
docker tag mock-server_ingresso:latest <account-id>.dkr.ecr.us-east-1.amazonaws.com/ingresso-mock-server:latest
docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/hkdl-mock-server:latest
docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/ingresso-mock-server:latest
```

### 방법 3: Lightsail Container (저렴한 고정 가격)

```bash
# 서비스 생성
aws lightsail create-container-service \
    --service-name mock-servers \
    --power small \
    --scale 1

# 이미지 푸시
aws lightsail push-container-image \
    --service-name mock-servers \
    --label hkdl \
    --image hkdl-mock-server:latest

aws lightsail push-container-image \
    --service-name mock-servers \
    --label ingresso \
    --image ingresso-mock-server:latest
```

## AWS 비용 추정

### EC2 t3.micro (프리티어 가능)
- **비용**: $0 (첫 12개월) 또는 월 ~$7.50
- **리소스**: 2 vCPU, 1GB RAM
- **추천**: 개발/테스트 환경

### ECS Fargate
- **비용**: 월 ~$12-15 (0.25 vCPU, 0.5GB per task)
- **추천**: 오토스케일링이 필요한 프로덕션 환경

### Lightsail Container Service
- **비용**: 월 $7 (Nano) ~ $40 (Small)
- **추천**: 고정 가격의 프로덕션 배포

## 프로덕션 체크리스트

### 보안
- [ ] 기본 인증 정보 변경
- [ ] HTTPS 적용 (nginx reverse proxy)
- [ ] Rate limiting 구현
- [ ] 인증 미들웨어 추가
- [ ] 방화벽 규칙 설정

### 모니터링
- [ ] CloudWatch 로그 설정 (AWS)
- [ ] Health check 알람 설정
- [ ] 컨테이너 메트릭 모니터링
- [ ] 로그 수집 시스템 구축

### 고가용성
- [ ] 로드 밸런서 사용
- [ ] 멀티 AZ 배포
- [ ] 오토스케일링 설정
- [ ] 상태 저장용 DB 구성 (필요시)

## 라이센스

테스트 목적의 Mock Server입니다.

## 문의

문제가 발생하면:
1. 로그 확인: `docker-compose logs`
2. 상태 확인: `curl http://localhost:5000/health`
3. 설정 파일 검토
4. 네트워크 연결 확인