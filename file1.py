print("file1")
print("file1")


def get_mask_account(user_account: str) -> str:
    """Функция, которая принимает на вход номер счета в виде числа и возвращает маску"""
    numbers_of_account = user_account.replace(" ", "")
    if len(numbers_of_account) == 20 and numbers_of_account.isdigit():
        mask_account = f"**{numbers_of_account[-4:]}"
        return mask_account
    else:
        return "Ошибка ввода номера счета!"

user_account = input()
print(get_mask_account(user_account))


def sort_by_date(info_about_users: list) -> list:
    info_users_copy = [item.copy() for item in info_about_users]
    for info_date in info_users_copy:
        info_only_date = widget.get_date(info_date["date"])
        info_date["date"] = info_only_date
    info_users_copy_sort = sorted(info_users_copy, reverse=True, key=lambda x: datetime.strptime(x["date"], "%d.%m.%Y"))
    for info_about_user in info_about_users:
        for info_user_copy_sort in info_users_copy_sort:
            if widget.get_date(info_about_user["date"]) == info_user_copy_sort["date"]:
                info_user_copy_sort["date"] = info_about_user["date"]
    return info_users_copy_sort


info_about_users = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
print(sort_by_date(info_about_users))