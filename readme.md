jquery django sqlite swiper bootstrap5

# fooorm

> 설문폼 서비스
>
> 장고를 학습하고 프레임워크의 소중함을 깨달을 수 있었던 토이 프로젝트입니다.

## Live demo

-

## Preview

![image](https://user-images.githubusercontent.com/72514247/128608326-8d6143c5-4e53-4dd0-b195-a6e1cd2daac1.png)

## Features

## 개발할 기능

- 문항 모델 (제목, 타입(), 타입에 따른 content)
- 생성된 문항을 볼 수 있는 사용자 폼 (문항, 연락처 기입후 확인 누르면 제출)
- 문항을 생성, 수정, 삭제, 볼수 있는 관리자 폼
  - 관리자 폼 (문항별 응답자 수, 선택지별 응답 비율, 응답자별 문항 응답)

## Tech and libraries

- django
- jquery
- sqlite
- toastr
- jquery.cookie

## Getting started

- use git clone.

```bash
$ cd Fooorm
$ python3 manage.py runserver (or python manage.py runserver)
```

- open http://localhost:8000/

## Note

This project is ongoing.

## License

This project is licensed under the MIT License - see the LICENSE.md for details
