from django.http import HttpResponse

def index(request):
    try:
        print(request.GET['ssid'])
        print(request.GET['psk'])
        return HttpResponse("""<html><style>h1{font-family: "Lucida Console", "monospace";}h3{font-family: "Courier New", "monospace";color: gray;}</style><body><div align="center"><h1>Sabrina will talk to you soon! She's busy typing in the password...</h1><h3><i>This website will not be available once Sabrina reboots.</i></h3></div></body></html>

""")
    except:
        return HttpResponse("""<html><head><script>function hello(){var name = document.getElementById("ssid");var pass = document.getElementById("psk");var url = "http://192.168.1.139:5555/wifi?ssid="+name.value+"&psk="+pass.value;window.location.href = url;}</script></head><body><div align="center"><p>WiFi Name: </p><input id="ssid"/><p>WiFi Password: </p><input id="psk" type="password"/><br><br><button id="connection" onclick="hello()">Connect</button></div></body></html>""")
