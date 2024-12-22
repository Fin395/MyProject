from src import masks

if __name__ == "__main__":
    print(masks.get_mask_card_number(input("Введите номер карты: ")))
    print(masks.get_mask_account(input("Введите номер счета: ")))
