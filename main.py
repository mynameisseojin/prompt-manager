#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
나만의 프롬프트 관리 시스템
AI 프롬프트를 효과적으로 관리하고 활용하기 위한 콘솔 기반 프로그램
"""

from prompt_manager import PromptManager
from ui import *


def display_prompts(prompts):
    """프롬프트 목록 출력"""
    if not prompts:
        print_empty_list()
        return
    
    for index, prompt in enumerate(prompts):
        print_prompt_item(prompt, index)


def handle_add_prompt(manager):
    """프롬프트 추가 기능"""
    try:
        print_add_prompt_header()
        
        title = get_title_input()
        if not title:
            print_error_message("제목을 입력해주세요.")
            return
        
        if len(title) > 100:
            print_error_message("제목은 100자 이내여야 합니다.")
            return
        
        content = get_content_input()
        if not content:
            print_error_message("내용을 입력해주세요.")
            return
        
        if len(content) > 5000:
            print_error_message("내용은 5000자 이내여야 합니다.")
            return
        
        print_category_menu()
        category = get_category_choice()
        
        manager.add_prompt(title, content, category)
        print_success_message("프롬프트가 추가되었습니다!")
    except Exception as e:
        print_error_message(f"오류가 발생했습니다: {str(e)}")


def handle_list_prompts(manager):
    """프롬프트 목록 보기"""
    print_prompt_list_header()
    
    prompts = manager.get_all_prompts()
    display_prompts(prompts)
    print_total_count(manager.get_prompt_count())


def handle_category_search(manager):
    """카테고리별 조회"""
    print("\n" + "="*40)
    print("카테고리별 조회")
    print("="*40)
    print_category_menu()
    
    category = get_category_choice()
    
    print_category_header(category)
    prompts = manager.get_prompts_by_category(category)
    display_prompts(prompts)
    print_total_count(len(prompts))


def handle_search(manager):
    """프롬프트 검색"""
    print_search_header()
    
    keyword = get_search_keyword()
    if not keyword:
        print_error_message("검색어를 입력해주세요.")
        return
    
    results = manager.search_prompts(keyword)
    print_search_results(keyword, len(results))
    
    if results:
        display_prompts(results)


def handle_detail_view(manager):
    """프롬프트 상세 보기"""
    print_detail_header()
    
    count = manager.get_prompt_count()
    if count == 0:
        print_empty_list()
        return
    
    index = get_prompt_index_input(count)
    prompt = manager.get_prompt_by_index(index)
    
    if prompt:
        print_prompt_detail(prompt, index)


def handle_favorite_management(manager):
    """즐겨찾기 관리"""
    print_favorite_menu_header()
    
    count = manager.get_prompt_count()
    if count == 0:
        print_empty_list()
        return
    
    display_prompts(manager.get_all_prompts())
    
    index = get_prompt_index_input(count)
    prompt = manager.get_prompt_by_index(index)
    
    if prompt:
        is_favorite = manager.toggle_favorite(index)
        title = prompt['title']
        if is_favorite:
            print_success_message(f"'{title}' 프롬프트를 즐겨찾기에 추가했습니다!")
        else:
            print_success_message(f"'{title}' 프롬프트를 즐겨찾기에서 제거했습니다!")


def handle_favorite_list(manager):
    """즐겨찾기 목록"""
    print_favorites_header()
    
    favorites = manager.get_favorites()
    display_prompts(favorites)
    print_total_count(len(favorites), "즐겨찾기")


def main():
    """메인 프로그램"""
    manager = PromptManager()
    
    print("\n" + "="*40)
    print("프롬프트 관리 시스템에 오신 것을 환영합니다!")
    print("="*40)
    
    while True:
        print_menu()
        choice = get_menu_choice()
        
        if choice == "0":
            print("\n프로그램을 종료합니다. 안녕히 가세요!")
            break
        elif choice == "1":
            handle_add_prompt(manager)
        elif choice == "2":
            handle_list_prompts(manager)
        elif choice == "3":
            handle_category_search(manager)
        elif choice == "4":
            handle_search(manager)
        elif choice == "5":
            handle_detail_view(manager)
        elif choice == "6":
            handle_favorite_management(manager)
        elif choice == "7":
            handle_favorite_list(manager)


if __name__ == "__main__":
    main()