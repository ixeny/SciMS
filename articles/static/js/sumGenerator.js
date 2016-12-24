function sumGen(){
	var article = document.getElementById("artContent");
	var summary = document.getElementById("tofcontents");
	if(summary != null){
		cpt = 1;

		mynav = document.createElement("nav");
		mynav.appendChild(genTheSum(article));
		summary.appendChild(mynav);
	}
}

function genTheSum(myarticle){
	list = document.createElement("ul");
	for (var i = 0; i < myarticle.childNodes.length; i++){
		if (myarticle.childNodes[i].tagName == "H2"){
			var li = document.createElement("li");
			var anch = document.createElement("a");

			anch.setAttribute("href", "#"+cpt);
			anch.appendChild(document.createTextNode(myarticle.childNodes[i].textContent));

			li.appendChild(anch);
			list.appendChild(li);
			myarticle.childNodes[i].setAttribute("id", cpt);
			cpt++;
		}
	}
	return list;
}

window.onload = sumGen;
