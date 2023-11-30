from collect.collect_daum_movie_review import review_collector
from db.movie_dao import get_last_review


def main():
    print("="*100)
    print("== 영화 리뷰 수집기 ==")
    print("="*100)
    movie_code = input("영화 코드>> ")  # 169328
    print("MSG: 매일 12시간에 수집")

    last_date = get_last_review()
    if last_date == None:  # 첫 리뷰인 경우
        last_date = 0
    else:
        last_date = int(last_date["int_regdate"])
    review_collector(movie_code, last_date)


if __name__ == "__main__":
    main()
