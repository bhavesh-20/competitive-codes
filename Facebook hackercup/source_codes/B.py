for _t in range(int(input())):
    n = int(input())
    arr = []
    rows, columns = [], []
    for _ in range(n):
        arr.append(list(input()))
    
    for row in arr:
        X, O, dot = row.count("X"), row.count("O"), row.count(".")
        rows.append(
            {
                "score": X - O,
                "available": dot,
            }
        )

    for column in range(n):
        score, available = 0, 0
        for row in range(n):
            if arr[row][column] == 'X':
                score += 1
            elif arr[row][column] == 'O':
                score -= 1
            else:
                available += 1
        columns.append(
            {
                "score": score,
                "available": available,
            }
        )

    minimum_replacement, distinct_sets = 10**18, 0
    for i in range(n):
        row = rows[i]
        if row["score"] + row["available"] == n:
            if minimum_replacement > row["available"]:
                minimum_replacement = row["available"]
                distinct_sets = 1
            elif minimum_replacement == row["available"]:
                distinct_sets += 1
        column = columns[i]
        if column["score"] + column["available"] == n:
            if minimum_replacement > column["available"]:
                minimum_replacement = column["available"]
                distinct_sets = 1
            elif minimum_replacement == column["available"]:
                distinct_sets += 1
    if minimum_replacement == 10**18:
        ans = "Impossible"
    else:
        if minimum_replacement == 0:
            ans = f"0 0"
        elif minimum_replacement == 1:
            distinct_set = set()
            for i in range(n):
                row = rows[i]
                if row["score"] + row["available"] == n and row["available"] == 1:
                    for j in range(n):
                        if arr[i][j] == '.':
                            distinct_set.add(n*i+j)
                            break
                column = columns[i]
                if column["score"] + column["available"] == n and column["available"] == 1:
                    for j in range(n):
                        if arr[j][i] == '.':
                            distinct_set.add(n*j+i)
                            break
            ans = f"1 {len(distinct_set)}"
        else:
            ans = f"{minimum_replacement} {distinct_sets}"
    print(f"Case #{_t+1}: {ans}")
