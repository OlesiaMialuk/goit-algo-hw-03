
import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(order):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-200, 100)  # Початкова позиція для малювання
    t.pendown()

    # Малюємо перший відрізок сніжинки
    for _ in range(3):
        koch_snowflake(t, order, 400)  # Розмір можна змінити за потреби
        t.right(120)

    window.mainloop()

# Введення користувача рівня рекурсії
order = int(input("Введіть рівень рекурсії (ціле число): "))

# Виклик функції для малювання сніжинки Коха
draw_koch_snowflake(order)
