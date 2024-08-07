import hashlib

def hash_string(input_string):
    hashes = {
        "MD5": hashlib.md5(input_string.encode()).hexdigest(),
        "SHA-1": hashlib.sha1(input_string.encode()).hexdigest(),
        "SHA-256": hashlib.sha256(input_string.encode()).hexdigest(),
        "SHA-384": hashlib.sha384(input_string.encode()).hexdigest(),
        "SHA-512": hashlib.sha512(input_string.encode()).hexdigest(),
    }

    for name, hash_value in hashes.items():
        #print(f"{name}: {hash_value} (Length: {len(hash_value)} characters)")
        #print(f"{name}: {hash_value} (Length: {len(hash_value)} characters)", input_string.encode())

# Exemplo de uso
#input_string = "Cybersecurity"

'''
input_string = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. In pulvinar vel elit quis rhoncus. Phasellus convallis nibh sit amet orci suscipit, nec dictum neque fermentum. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aliquam egestas tortor in felis tempor congue eget non lacus. Aenean tempor ante quis lobortis feugiat. Vivamus auctor tristique ultrices. Duis et dictum nisi. Phasellus imperdiet urna eu pulvinar ornare. Morbi et mauris purus. Maecenas semper, justo et bibendum efficitur, lectus nibh dignissim risus, eu convallis odio nisl quis dolor.

Aliquam id semper sapien. Maecenas maximus ullamcorper ipsum, ac aliquet sapien accumsan quis. Quisque interdum elementum enim, ut lobortis lectus eleifend ac. Quisque at sollicitudin mi. Vivamus vestibulum sem tortor, vel rutrum odio efficitur quis. In vitae ipsum sollicitudin, finibus leo ut, venenatis enim. Cras id magna magna.

Suspendisse sed velit pellentesque augue aliquet condimentum a eu mi. Pellentesque aliquam mi sit amet maximus pulvinar. Curabitur vulputate turpis at augue malesuada, non vestibulum lorem pellentesque. Vivamus sollicitudin dolor a nisi interdum, vel viverra ex molestie. Nam metus dolor, eleifend nec ligula facilisis, bibendum fermentum magna. Nunc bibendum erat et ipsum interdum blandit. Nunc hendrerit, eros ut volutpat pharetra, orci lorem pharetra elit, eu tincidunt dui tortor sit amet urna. Aenean ac placerat quam, in cursus urna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Morbi dignissim tellus quis neque venenatis aliquet. Maecenas sodales quam mi, nec dapibus urna sodales in. Proin arcu lorem, sagittis eu tempor at, pretium in nulla. Integer condimentum at augue id tempus. Sed quis tempus leo.

Aliquam nec est bibendum, consequat risus ac, scelerisque metus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Sed ultrices enim vitae nibh mollis dignissim. Vestibulum viverra mauris nec quam fermentum consequat. Fusce at felis urna. In lectus nunc, semper a lacinia vitae, ornare quis lectus. Pellentesque sodales neque non est sagittis sagittis.

Fusce non diam nibh. Curabitur tempus mi ipsum, a consequat eros dictum ac. Praesent tortor nunc, efficitur id nisl sed, dapibus sodales ligula. Suspendisse tempor suscipit nisi a venenatis. Vivamus in enim nec nisl facilisis luctus. Sed placerat porttitor ligula, ac sagittis quam consequat quis. Duis laoreet elit placerat arcu accumsan, vitae fermentum mi accumsan."""
'''

hash_string(input_string)
