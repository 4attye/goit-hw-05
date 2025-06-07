import timeit
from algorithms import kmp_search, boyer_moore_search, rabin_karp_search

articles = []
substrings_list = [["потрібно", "СУБД"],["car_1", "car_2"]]
titles = ["Час виконання пошуку підрядків у статтях з використанням існуючих підрядків:",
          "Час виконання пошуку підрядків у статтях з використанням не існуючого підрядка:"]


with open('article_1.txt', 'r', encoding="UTF-8") as f_1:
    articles.append(f_1.read())

with open('article_2.txt', 'r', encoding="UTF-8") as f_2:
    articles.append(f_2.read())


for substrings, title in zip(substrings_list, titles):
    print(f"\n{title}")
    for i, substring in enumerate(substrings):
        print(f"\nПідрядок для пошуку: '{substring}' у статті {i+1}")
        print(f"{f"Знайдено підрядок на позиції {kmp_search(articles[i], substring)}" if kmp_search(articles[i], substring) != -1 else "Підрядок не знайдено"}")
        t_kmp_search_article = timeit.timeit(
            lambda: kmp_search(articles[i], substring)
            , number=1)
        print(f"Час виконання KMP для статті {i+1}: {t_kmp_search_article:.5f} секунд")

        t_boyer_moore_search_article = timeit.timeit(
            lambda: boyer_moore_search(articles[i], substring)
            , number=1)
        print(f"Час виконання Boyer-Moore для статті {i+1}: {t_boyer_moore_search_article:.5f} секунд")

        t_rabin_karp_search_article = timeit.timeit(
            lambda: rabin_karp_search(articles[i], substring)
            , number=1)
        print(f"Час виконання Rabin-Karp для статті {i+1}: {t_rabin_karp_search_article:.5f} секунд")