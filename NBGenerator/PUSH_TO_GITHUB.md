# GitHub에 Push하는 방법

## 1단계: Git 저장소 초기화 (아직 안 했다면)

```bash
cd /Users/hyunko/Desktop/git/NBGenerator
git init
```

## 2단계: 파일 추가 및 첫 커밋

```bash
# 모든 파일 추가
git add .

# 첫 커밋
git commit -m "Initial commit: NBGenerator module"
```

## 3단계: GitHub에서 새 리포지토리 생성

1. GitHub 웹사이트에 로그인
2. 우측 상단의 `+` 버튼 클릭 → `New repository` 선택
3. Repository name 입력 (예: `NBGenerator`)
4. Public 또는 Private 선택
5. **"Initialize this repository with a README" 체크하지 않기** (이미 로컬에 파일이 있으므로)
6. `Create repository` 클릭

## 4단계: Remote 추가 및 Push

GitHub에서 리포지토리를 생성한 후, 제공되는 명령어를 사용하거나 아래 명령어를 사용하세요:

```bash
# GitHub 리포지토리 URL로 변경 (예: https://github.com/your-username/NBGenerator.git)
git remote add origin https://github.com/YOUR_USERNAME/NBGenerator.git

# 기본 브랜치를 main으로 설정 (필요한 경우)
git branch -M main

# GitHub에 push
git push -u origin main
```

## 전체 명령어 한 번에 실행

```bash
cd /Users/hyunko/Desktop/git/NBGenerator

# Git 초기화 (이미 되어 있다면 스킵)
git init

# 파일 추가 및 커밋
git add .
git commit -m "Initial commit: NBGenerator module"

# Remote 추가 (YOUR_USERNAME을 실제 GitHub 사용자명으로 변경)
git remote add origin https://github.com/hyun-ko-DS/NBGenerator.git

# 브랜치 이름 설정
git branch -M main

# Push
git push -u origin main
```

## 주의사항

- `.env` 파일은 `.gitignore`에 포함되어 있어 자동으로 제외됩니다
- `output/` 폴더와 `__pycache__/` 폴더도 제외됩니다
- GitHub에 push하기 전에 `.env` 파일에 API 키가 포함되어 있지 않은지 확인하세요

