regions = {
    "云南": {
        "昆明": ["五华区", "盘龙区", "官渡区"],
        "大理": ["大理市", "洱源县"]
    },
    "广东": {
        "广州": ["天河区", "越秀区", "海珠区"],
        "深圳": ["南山区", "福田区", "罗湖区"]
    }
}
while True:
    provinces = list(regions.keys())
    print("=== 请选择省 ===（输入 0 退出程序）")
    for idx, p in enumerate(provinces, start=1):
        print(f"{idx}. {p}")
    choice = input("请输入省的编号：")
    if choice == "0":
        break
    try:
        choice_int = int(choice)
        selected_province = provinces[choice_int - 1]
    except (ValueError, IndexError):
        print("请输入列表中的数字！")
        continue
    print(f"你选择了{choice_int}.{selected_province}")

    while True: #选城市
        cities_dict = regions[selected_province]
        cities = list(regions[selected_province].keys())
        print(f"===请选择{selected_province}省中的市===（输入 0 返回上一级菜单）")
        for idx, city in enumerate(cities, start=1):
            print(f"{idx}. {city}")
        city_choice = input("请输入城市编号：")
        if city_choice == "0":
            break
        try:
            city_choice_int = int(city_choice)
            selected_city = cities[city_choice_int - 1]
        except (ValueError, IndexError):
            print("请输入列表中的数字！")
            continue
        print(f"你选择了{city_choice_int}.{selected_city}")

        while True: #选区县
            xians = regions[selected_province][selected_city]
            print(f"===请选择{selected_city}市中的县（输入 0 返回上一级菜单）===")
            for idx, xian in enumerate(xians, start=1):
                print(f"{idx}. {xian}")
            xian_choice = input("请输入区县编号：")
            if xian_choice == "0":
                break
            try:
                xian_choice_int = int(xian_choice)
                selected_xian = xians[xian_choice_int - 1]
            except (ValueError, IndexError):
                print("请输入列表中的数字！")
                continue
            print(f"你选择了{xian_choice_int}. {selected_xian}")
            print(f"现在位于{selected_province} - {selected_city} - {selected_xian}")
            xian_choice = input("输入 0 返回上一级菜单")
            if xian_choice == "0":
                break
print("byebye!")