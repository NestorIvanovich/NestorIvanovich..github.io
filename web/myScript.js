
let englishWord = 'ddk';
let rusWord;
async function getWord () {
         englishWord = await eel.translate_before()();
         rusWord = await eel.translate_after(englishWord)();
        document.getElementById("pythonInput").innerText = rusWord;
        
        }
function examination () {
    
     let result = englishWord.toLowerCase() === getInputValue();

        if (result){
       oknotrue.toggle();
       btnNext.onclick = getWord;
       document.getElementById("userInput").value = "";
        }else{
        oknofalse.show();
    }
    }
    function getInputValue(){
        // Выбор элемента input и получение его значения
        let inputVal = document.getElementById("userInput").value;
        return inputVal.toLowerCase()
    }

 document.addEventListener("DOMContentLoaded", getWord);
  
 document.getElementById("submit").addEventListener("click", examination);
 
 
    document.getElementById("reset").onclick = getWord;

    const oknotrue = new bootstrap.Modal(document.getElementById('staticBackdrop'), {keyboard: false, backdrop: 'static'});
    const oknofalse = new bootstrap.Modal(document.getElementById('staticBackdropFail'), {keyboard: false, backdrop: 'static'});
    const btnNext = document.getElementById('btnNext');
    const notBtnNext = document.getElementById('notBtnNext');

    
 
