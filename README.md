## Table of Contents
- [Part 1. 프로젝트 소개](#1-프로젝트-소개)
- [Part 2. 사용 기술 스택](#2-사용-기술-스택)
- [Part 3. 주요 기능](#3-주요-기능)
- [Part 4. 기본 기능](#4-기본-기능)
- [Part 5. 주요 이슈](#5-주요-이슈)
- [Part 6. 보완할 점](#6-보완할-점)

# 1. 프로젝트 소개
- The Rank of Korea (2021)
- 언론형 커뮤니티 플렛폼에 게임성(레벨링, 아이템)을 더한 개인 프로젝트 입니다.
- https://therok.net
# 2. 사용 기술 스택
- Django
- Ajax
- Python
- JavaScript
- AWS EC2(Windows)
# 3. 주요 기능
- 커뮤니티형 게시판과 댓글, 답글 기능 및 추천순으로 TOP3 댓글 고정 기능
- 게시글 추천 기능 개발(현실버전 추천과 반대/ 조선시대 창과 방패) - AJAX를 이용한 비동기 처리
- 현실에서는 고정닉네임을 사용하고 조선시대에서는 글을 쓸 때마다 랜덤 닉네임을 부여하는 기능
- 화면 상단에 어제와 비교해 오늘 새로 가입한 회원들의 정치 성향을 파악하고 전체 회원 정치성향 분포를 실시간으로 알려주는 기능
-  shop / 아이템 구매  회원 전체가 사용 가능한 기본 아이템 7개와 각 부서별로 사용가능한 스페셜 아이템 10개 기능 개발
- LEVEL UP - 조선시대 관직과 품계를 모델으로하는 회원 레벨링 시스템 
# 4. 기본 기능
- 로그인
- 회원가입
- 프로필 보기 / 수정
- 스크랩
- 인벤토리
# 5. 주요 이슈
- debug toolbar로 쿼리 중복최소화 제거하고
- 게시글 도배 방지
- manytomany 필드 버튼 누르면 페이지 다시 가져와서 로딩가지니깐 spa로 ajax 비동기 구현
- top 고정배너에 정치선호분포 포현 이슈(celery, threading, schedule, apschedule 중에서 apschedule 사용)
# 6. 보완할 점
