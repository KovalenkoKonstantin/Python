# Напиши программу,
# которая считает 2 строки и выведет "YES" (без кавычек),
# если они равны (игнорируя регистр), и "NO" (без кавычек), иначе.

if input().upper() == input().upper():
    print('YES')
else:
    print('NO')

print('YES' if input().lower() == input().lower() else 'NO')
