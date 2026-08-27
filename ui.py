from constants import CATEGORIES


def print_menu():
    """메인 메뉴 출력"""
    print("\n" + "="*40)
    print("나만의 프롬프트 관리")
    print("="*40)
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")
    print("="*40)


def get_menu_choice():
    """메뉴 선택 입력"""
    while True:
        try:
            choice = input("선택: ").strip()
            if choice in ['0', '1', '2', '3', '4', '5', '6', '7']:
                return choice
            else:
                print("❌ 0-7 사이의 숫자를 입력해주세요.")
        except KeyboardInterrupt:
            print("\n프로그램을 종료합니다.")
            exit()


def print_category_menu():
    """카테고리 선택 메뉴 출력"""
    print("\n카테고리 선택:")
    for key, value in CATEGORIES.items():
        print(f"{key}) {value}")


def get_category_choice():
    """카테고리 선택 입력"""
    while True:
        try:
            choice = input("선택: ").strip()
            if choice in CATEGORIES:
                return CATEGORIES[choice]
            else:
                print("❌ 1-6 사이의 숫자를 입력해주세요.")
        except KeyboardInterrupt:
            print("\n프로그램을 종료합니다.")
            exit()


def print_add_prompt_header():
    """프롬프트 추가 헤더 출력"""
    print("\n" + "="*40)
    print("프롬프트 추가")
    print("="*40)


def print_prompt_list_header(count=None):
    """프롬프트 목록 헤더 출력"""
    print("\n" + "="*40)
    print("프롬프트 목록")
    print("="*40)


def print_category_header(category, count=None):
    """카테고리별 조회 헤더 출력"""
    print("\n" + "="*40)
    print(f"[{category}] 카테고리 프롬프트:")
    print("="*40)


def print_search_header():
    """검색 헤더 출력"""
    print("\n" + "="*40)
    print("프롬프트 검색")
    print("="*40)


def print_search_results(keyword, count):
    """검색 결과 요약"""
    print(f"\n검색 결과: '{keyword}'")
    if count == 0:
        print("검색 결과가 없습니다.")
    else:
        print(f"{count}개의 프롬프트를 찾았습니다.")


def print_detail_header():
    """상세 보기 헤더 출력"""
    print("\n" + "="*40)
    print("프롬프트 상세 보기")
    print("="*40)


def print_prompt_detail(prompt, index):
    """프롬프트 상세 정보 출력"""
    print("\n" + "-"*40)
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    favorite_mark = "⭐" if prompt['favorite'] else "☆"
    print(f"즐겨찾기: {favorite_mark}")
    print("-"*40)
    print("내용:")
    print(prompt['content'])
    print("-"*40)


def print_favorite_menu_header():
    """즐겨찾기 관리 헤더 출력"""
    print("\n" + "="*40)
    print("즐겨찾기 관리")
    print("="*40)


def print_favorites_header():
    """즐겨찾기 목록 헤더 출력"""
    print("\n" + "="*40)
    print("즐겨찾기 목록")
    print("="*40)


def print_prompt_item(prompt, index):
    """프롬프트 항목 출력 (리스트용)"""
    favorite_mark = "⭐" if prompt['favorite'] else ""
    print(f"{index + 1}. [{prompt['category']}] {prompt['title']} {favorite_mark}".strip())


def print_total_count(count, message="프롬프트"):
    """총 개수 출력"""
    print(f"\n총 {count}개의 {message}")


def print_success_message(message):
    """성공 메시지 출력"""
    print(f"\n✅ {message}")


def print_error_message(message):
    """오류 메시지 출력"""
    print(f"\n❌ {message}")


def get_title_input():
    """프롬프트 제목 입력"""
    return input("제목: ").strip()


def get_content_input():
    """프롬프트 내용 입력"""
    print("내용 입력 (완료 후 Enter 두 번):")
    lines = []
    empty_count = 0
    while empty_count < 1:
        line = input()
        if line == "":
            empty_count += 1
        else:
            empty_count = 0
            lines.append(line)
    return "\n".join(lines).strip()


def get_prompt_index_input(max_index):
    """프롬프트 번호 입력"""
    while True:
        try:
            index = int(input("프롬프트 번호 입력: ").strip())
            if 1 <= index <= max_index:
                return index - 1  # 0-based index로 변환
            else:
                print(f"❌ 1-{max_index} 사이의 숫자를 입력해주세요.")
        except ValueError:
            print("❌ 숫자를 입력해주세요.")


def get_search_keyword():
    """검색 키워드 입력"""
    return input("검색어: ").strip()


def print_empty_list(message="프롬프트가 없습니다."):
    """빈 목록 메시지"""
    print(f"\n{message}")


def validate_title(title):
    """제목 유효성 검증"""
    return len(title.strip()) > 0 and len(title) <= 100


def validate_content(content):
    """내용 유효성 검증"""
    return len(content.strip()) > 0 and len(content) <= 5000


def is_valid_category(category_key):
    """카테고리 유효성 검증"""
    return category_key in CATEGORIES


def print_advanced_search_menu():
    """고급 검색 메뉴"""
    print("\n고급 검색 옵션:")
    print("1) 제목으로만 검색")
    print("2) 내용으로만 검색")
    print("3) 카테고리와 키워드로 검색")
    print("0) 돌아가기")


def get_search_option():
    """검색 옵션 선택"""
    while True:
        try:
            choice = input("선택: ").strip()
            if choice in ['0', '1', '2', '3']:
                return choice
            else:
                print("❌ 0-3 사이의 숫자를 입력해주세요.")
        except KeyboardInterrupt:
            return '0'


def print_search_options():
    """검색 옵션 표시"""
    print("\n검색 옵션:")
    print("1) 기본 검색 (제목+내용)")
    print("2) 고급 검색")
    print("0) 돌아가기")


def get_basic_search_choice():
    """기본/고급 검색 선택"""
    while True:
        try:
            choice = input("선택: ").strip()
            if choice in ['0', '1', '2']:
                return choice
            else:
                print("❌ 0-2 사이의 숫자를 입력해주세요.")
        except KeyboardInterrupt:
            return '0'