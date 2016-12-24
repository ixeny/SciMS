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
};

var xhr= createXhrObject();

function getResponse(pid){
  xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
	var obj = JSON.parse(this.responseText);
    myStr="";
    document.getElementById("cats_articles").innerHTML = myStr;
	for (var i = 0; i < obj.length; i++){
	    var art = obj[i];
	     myStr+= "<a href=\"/articles/view/"+art.pk+"/\" class=\"list-group-item\">"+art.fields.title+"</a>";
    }
    document.getElementById("cats_articles").innerHTML = myStr;
    }
  };
  xhr.open("GET", "/categories/"+pid, true);
  xhr.send();
};




function insertAtCursor(myField, myValue) {
    //IE support
    if (document.selection) {
        myField.focus();
        sel = document.selection.createRange();
        sel.text = myValue;
    }
    //MOZILLA and others
    else if (myField.selectionStart || myField.selectionStart == '0') {
        var startPos = myField.selectionStart;
        var endPos = myField.selectionEnd;
        myField.value = myField.value.substring(0, startPos)
            + myValue
            + myField.value.substring(endPos, myField.value.length);
    } else {
        myField.value += myValue;
    }
}



function putContent(myField) {
 return insertAtCursor(myField, '\\tableofcontents')
}



function putSection(myField, myValue) {
    return insertAtCursor(myField, '\n\\section{'+myValue+'}')
}


function putSubSection(myField, myValue) {
  return insertAtCursor(myField, '\n\\subsection{'+myValue+'}')
}



function putFormula(myField, myValue) {
   return insertAtCursor(myField, '\n['+myValue+']')
}


function putImage(myField, myValue) {
 return insertAtCursor(myField, '\n{%'+myValue+'%}')
}
