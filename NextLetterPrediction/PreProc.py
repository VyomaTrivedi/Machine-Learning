f = open("movie_lines.txt", "r")
g = open("sample_cleaned.txt", "w")

for line in f:
    if line.strip():
        g.write("\t".join(line.split()[8:]) + "\n")

f.close()
g.close()
