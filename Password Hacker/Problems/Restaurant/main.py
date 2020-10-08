import itertools

main_dict = {}
for d, p in zip(main_courses, price_main_courses):
    main_dict[d] = p
dessert_dict = {}
for d, p in zip(desserts, price_desserts):
    dessert_dict[d] = p
drinks_dict = {}
for d, p in zip(drinks, price_drinks):
    drinks_dict[d] = p
for main, dessert, drink in itertools.product(main_dict.items(), dessert_dict.items(), drinks_dict.items()):
    total = main[1] + dessert[1] + drink[1]
    if total <= 30:
        print('{} {} {} {}'.format(main[0], dessert[0], drink[0], str(total)))
