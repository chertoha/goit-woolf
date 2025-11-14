org 0x100                 ; .COM-програма, початкова адреса

section .data
    a db 4                ; Значення змінної a
    b db 7                ; Значення змінної b
    c db 2                ; Значення змінної c
    msg db 'Answer is: $' ; Повідомлення перед числом

section .text
start:
    ; Обчислення виразу: b - c + a
    mov al, [b]           ; AL = b
    sub al, [c]           ; AL = b - c
    add al, [a]           ; AL = b - c + a

    ; Перетворення результату в ASCII
    add al, '0'           ; AL = ASCII-символ цифри

    ; Вивід рядка "Answer is: "
    mov dx, msg
    mov ah, 09h
    int 21h

    ; Вивід результату
    mov dl, al
    mov ah, 02h
    int 21h

    ; Завершення програми
    mov ax, 4C00h
    int 21h
