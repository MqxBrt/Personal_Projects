var GlobalR5; //contient R5.txt
var GlobalLoaded = false;

//charge r5 lors du démarrage de la page
async function loadR5() {
  setDisable(true);
  //remplit GlobalR5 si GlobalR5 est vide
  if (typeof GlobalR5 == 'undefined') {
    GlobalR5 = await recupereDonneesR5();
    GlobalR5+=''; //pour transformer de "object" à "string"
    GlobalR5 = trier_r5(GlobalR5);
  }
  GlobalLoaded = true;
  console.log("r5_syn.txt ready")
  setDisable(false);
}

//récupère le texte à paraphraser
function getOldText() {
  var stringText = "";
  stringText = document.getElementById("txtOG").value;
  return stringText;
}

//affiche le texte paraphrasé
function setNewText(newText) {
  document.getElementById("txtED").value = newText;
}

//défini le statut du bouton selon le statut du générateur
function setDisable(state) {
  document.getElementById("startParaphrase").disabled = state; 
}

//force les valeurs du pourcentage
function forceMinMax(percent) {
  if (percent.value != "") {
    if (parseInt(percent.value) < parseInt(percent.min)) {
      percent.value = percent.min;
    }
    if (parseInt(percent.value) > parseInt(percent.max)) {
      percent.value = percent.max;
    }
  }
}

//récupère le pourcentage
function getPercentP() {
  if (document.getElementById("percentP").value == "") {
    return 100;
  }
  else {
    return document.getElementById("percentP").value;
  }
}

function isUpperCase(word) {
  return word.toUpperCase() === word;
}

//lance le paraphrasage
async function handleClick() {
  var form = document.getElementById("boutonPARA");
  function handleForm(event) { 
    event.preventDefault(); 
  } 
  form.addEventListener('submit', handleForm);
  if (GlobalLoaded) {
    setDisable(true);
    setNewText("");
    if (getOldText() !== "") {
      setNewText(changeWords(getOldText(), removeUnwanted(tableauSynonymes(spotWords(getOldText().toString()), GlobalR5)), getPercentP()));
    }
    setDisable(false);
  }
  else {
    alert("Fichier de synonymes en chargement, veuillez patienter")
  }
}

//choisis le synonyme de chaque mot et le remplace
function changeWords(texteOriginal, synonymes, pourcentageParaphrase) {
  var texteDebut = "";
  var texteFin = texteOriginal;

  //choix des mots à paraphraser en fonction du pourcentage
  nombreChangements = Math.ceil(synonymes.length * (pourcentageParaphrase / 100)); //nombre de mots à changer en fonction du pourcentage
  var deciderTab = [];
  var cpt = 0;
  for (var i = 0; i < synonymes.length; i++) {
    deciderTab.push(0);
  }
  while (cpt < nombreChangements) {
    var randomC = Math.floor(Math.random() * (synonymes.length));
    if (deciderTab[randomC] == 0) {
      deciderTab[randomC] = 1;
      cpt++;
    }
  }

  //changement des mots par leur synonyme aléatoire
  var exceptions = [""," ",".",",",";","\"","!","(",")","-","?"];
  for (var i = 0; i < synonymes.length; i++) { 
    if (texteFin === "") {
      return texteDebut;
    }   
    if (deciderTab[i] == 1) {
      var wordSize = synonymes[i][0].length; //taille du mot
      var wordBegin = texteFin.search(synonymes[i][0]); //début du mot
      if (wordBegin == -1) {
        var wordUperCase = synonymes[i][0].slice(0, 1).toUpperCase() + synonymes[i][0].slice(1, synonymes[i][0].length);
        wordBegin = texteFin.search(wordUperCase);
      }
      if (wordBegin == -1) {
        var wordCapsLock = synonymes[i][0].toUpperCase();
        wordBegin = texteFin.search(wordCapsLock);
      }
      var wordEnd = wordBegin + wordSize; //fin du mot
      if (wordBegin != -1) {
        if (exceptions.includes(texteFin.charAt(wordEnd)) && exceptions.includes(texteFin.charAt(wordBegin - 1))) {
          var randomSynonymeI = Math.floor(Math.random() * (synonymes[i].length - 1) + 1);
          if (isUpperCase(texteFin.slice(wordBegin, wordEnd))) {
            texteDebut = texteDebut + texteFin.slice(0, wordBegin) + synonymes[i][randomSynonymeI].toUpperCase();
            texteFin = texteFin.slice(wordEnd);
          }
          else if (isUpperCase(texteFin.charAt(wordBegin))) {
            texteDebut = texteDebut + texteFin.slice(0, wordBegin) + synonymes[i][randomSynonymeI].slice(0, 1).toUpperCase() + synonymes[i][randomSynonymeI].slice(1, synonymes[i][randomSynonymeI].length);
            texteFin = texteFin.slice(wordEnd);
          }
          else {
            texteDebut = texteDebut + texteFin.slice(0, wordBegin) + synonymes[i][randomSynonymeI];
            texteFin = texteFin.slice(wordEnd);
          }
        }
        else {
          i--;
          texteDebut = texteDebut + texteFin.slice(0, wordEnd);
          texteFin = texteFin.slice(wordEnd);
        }
      }
    }
  }

  var texteParaphrase = texteDebut + texteFin;
  console.log("paraphrase done");
  return texteParaphrase;
}

async function recupereDonneesR5(){
  //si une erreur apparait à tabSyn[0] ligne 166, changez l'URL ci-dessous avec le nouveau du fichier r5_syn via : http://www.jeuxdemots.org/jdm-about.php
  url="https://limitless-hollows-85749.herokuapp.com/https://www.jeuxdemots.org/JDM-LEXICALNET-FR/02232022-LEXICALNET-JEUXDEMOTS-R5.txt";
  try {
    const response  = await fetch(url)
    const buffer = await response.arrayBuffer()
    const decoder = new TextDecoder('iso-8859-1')
    const text = decoder.decode(buffer)
    return text
  } catch (err) {
    console.log(err)
  }
}

function trier_r5(R5){
  var tabSyn = R5.split(";\n"); //tableau des synonymes (tableau simple)
  tabSyn.shift(); //enleve l'en tete du .txt dont on n'a pas besoin
  tabSyn[0] = tabSyn[0].slice(1,tabSyn[0].length); //enlève le \n de trop au début 
  for (let i = 0; i < tabSyn.length; i++)
  {
    tabSyn[i] = tabSyn[i].split(";");//mise sous forme tableau de tableaux, 1 tableau par synonyme
  }
  //console.log(tabSyn); //2 791 702 arrays
  for (let i = 0; i < tabSyn.length; i++)//
  {
      if(tabSyn[i][2]>=20)//poids suffisant, on garde le mot
    {
      tabSyn[i].pop(); //on enlève le poids
    }
    else //poids trop faible, on enlève le mot
    {
      delete tabSyn[i];//marche
      //tabSyn.splice(i,1);//ne marche pas??
    }
  }
  
   tabSyn = tabSyn.filter(function (el) {//pour enlever les "undefined" suite au delete juste en haut
    return el != null;
    });
  //console.log(tabSyn); //2 491 468 arrays (-300k arrays)
  var motbuffer = tabSyn[0][0]; //premier mot 
  var tabBuffer = [];
  tabBuffer.push(motbuffer, tabSyn[0][1]) //premier mot et premier synonyme dans l'array buffer
  var tabFinal = [];

  for (var i = 1; i < tabSyn.length; i++) //maintenant on veut tous les synonymes pour chaque mot
  {
      if(motbuffer == tabSyn[i][0]) //cas où on le mot buffer est toujours le même
      {
        tabBuffer.push(tabSyn[i][1]);
      }
      else //cas où le mot buffer a changé => on push l'array buffer et on change le mot buffer
      {
        tabFinal.push(tabBuffer);
        motbuffer = tabSyn[i][0];
        tabBuffer = []; //reset de l'array buffer
        tabBuffer.push(motbuffer, tabSyn[i][1]);
      }
  }
  tabFinal.push(tabBuffer); //on sort de la boucle avant de pouvoir push le dernier mot, donc on le fait ici
  return tabFinal;//1 685 000 arrays
}

//divise le texte original en tableau de mots
function spotWords(text) {
  text = text.toLowerCase();
  const regex1 = /["\"!#$%&()*+,./:;<=>?@[\]^_`{|}~§\\"]/g;
  const regex2 = /["\n"]/g;
  var str1 = text.replace(regex1, '');
  var str2 = str1.replace(regex2, " ");
  var str3 = str2.split(" ");
  return str3;
}

//renvoie le tableau de synonymes pour changeWords()
function tableauSynonymes(words, r5) {
  var resTab = [];
  for (var i = 0; i < words.length; i++) {
    var j = 0;
    var found = false;
    while (!found) {
        found = (r5[j][0] == words[i])
        if ((j != r5.length) && (!found)) {
          j++;
        }
        if ((j == r5.length) && (!found)) {
          j = -1;
          found = true;
        }
    }
    if (j != -1) {
      resTab.push(r5[j]);
    }
  }
  return resTab;
}

function removeUnwanted(tab) {
  var noWords = ["Je","je","Tu","tu","Il","il","Elle","elle","On","on","Nous","nous","Vous","vous","Ils","ils","Elles","elles","lui","ne","se","ce","du","un","est","peu","qui","que","sans","et","seulement","des","son","sa","plus","de","mais","ou","donc","or","ni","car","dans","à","me","te","se","sur","chez","allé"];
  var tempTab = [];
  for (var i = 0; i < tab.length; i++) {
    var j = 0;
    var size = tab[i].length;
    while (j < size) {
      if (tab[i][j].includes("en:") || tab[i][j].includes(">") || tab[i][j].includes("_") || noWords.includes(tab[i][0])) {
        j = size;
        for (var k = 0; k < tab.length; k++) {
          if (k != i) {
            tempTab.push(tab[k]);
          }
        }
        tab = tempTab;
        tempTab = [];
        i--;
      }
      else {
        j++;
      }
    }
  }
  return tab;
}
