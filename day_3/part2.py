
matrix = {}
data = (tuple(int(x) for x in line.split(',')) for line in open('input.txt'))

all_claims = set()
touched = set()

for claim_id, x_off, y_off, width, height in data:
    all_claims.add(claim_id)
    for x in range(x_off, x_off + width):
        for y in range(y_off, y_off + height):
            claims = matrix.setdefault((x, y), set())
            if claims:
                touched.update(claims)
                touched.add(claim_id)
            claims.add(claim_id)



print(all_claims - touched)