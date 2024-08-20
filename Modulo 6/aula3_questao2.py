# Lista de URLs
urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

# Cria a lista de domínios
dominios = [url[4:-4] for url in urls]

# Imprime a lista de domínios
print("dominios:", dominios)