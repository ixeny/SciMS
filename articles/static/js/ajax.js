function createXhrObject() {
     if (window.XMLHttpRequest)
          return new XMLHttpRequest();
 
	if (window.ActiveXObject) {
        var names = [
            "Msxml2.XMLHTTP.6.0",
            "Msxml2.XMLHTTP.3.0",
            "Msxml2.XMLHTTP",
            "Microsoft.XMLHTTP"
        ];
        for(var i in names) {
            try {
                 return new ActiveXObject(names[i]); 
            } catch(e) {}
        }
    }
    return null; // not supported
}


