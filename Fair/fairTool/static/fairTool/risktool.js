$(document).ready(function(){
    var button = document.createElement("button");
    button.innerHTML = "Submit";

    var body = document.getElementsByTagName("body")[0];
    body.appendChild(button);

    function tefInherent(tefInherent){
        var tefInherent = cfaInheritent + padInherent;
        if (tefInherent < 5){
            print("1");
        }
        else if (tefInherent == 5){
            print("2");
        }
        else if (tefInherent == 6){
            print("3");
        }
        else if (tefInherent == 7){
            print("4");
        }
        else if (tefInherent > 7){
            print("5");
        }
        else;{
                print("undefined");
        }  
    }
    
    function vInherent(vInherent){
        var vInherent= cfaInheritent + padInherent;
        if (vInherent < 5){
            print("1");
        }
        else if (vInherent == 5){
                print("2");
        }
        else if (vInherent == 6){
            print("3");
        }
        else if (vInherent == 7){
            print("4");
        }
        else if (vInherent > 7){
            print("5");
        }
        else;{
                print("undefined");
        }
    }
    
    function plefInherent(plefInherent){
        var plefInherent = tefInherent + vInherent
        if (plefInherent < 5){
            print("1");
        }
        else if (plefInherent == 5){
            print("2");
        }
        else if (plefInherent == 6){
            print("3");
        }
        else if (plefInherent == 7){
            print("4");
        }
        else if (plefInherent > 7){
            print("5");
        }
        else;{
                print("undefined");
        }
    }
    
    function prInherent(prInherent){
        var prInherent = plefInherent + plmrInheritent
        if (prInherent < 5){
            print("Very Low");
        }
        else if (prInherent == 5){
            print("Low");
        }
        else if (prInherent == 6){
            print("Medium");
        }
        else if (prInherent == 7){
            print("High");
        }
        else if (prInherent > 7){
            print("Very High");
        }
        else;{
                print("undefined");
        }
    }
    
    function slefInherent(slefInherent){
        var slefInherent = plefInherent + slpPercent
        if (plefInherent < 5){
            print("1");
        }
        else if (plefInherent == 5){
            print("2");
        }
        else if (plefInherent == 6){
            print("3");
        }
        else if (plefInherent == 7){
            print("4");
        }
        else if (plefInherent > 7){
            print("5");
        }
        else;{
                print("undefined");
        }
    }
    
    function srInherent(srInherent){
        var srInherent = slmrInheritent + slefInherent
        if (srInherent < 5){
            print("Very Low");
        }
        else if (srInherent == 5){
            print("Low");
        }
        else if (srInherent == 6){
            print("Medium");
        }
        else if (srInherent == 7){
            print("High");
        }
        else if (srInherent > 7){
            print("Very High");
        }
        else;
                print("undefined");
    }
    
    function overallRisk(overallRisk){
        var overallRisk = prInherent + srInherent
        if (prInherent < 5 , srInherent < 5){
            print("Very Low");
        }
        else if  (prInherent < 5, srInherent == 5){
            print("Low");
        }
        else if (prInherent < 5, srInherent == 6){
            print("Medium");
        }
        else if (prInherent < 5, srInherent == 7){
            print("High");
        }
        else if (prInherent < 5, srInherent > 7){
            print("Very High");
        }
        else if (prInherent == 5, srInherent < 5){
            print("Low");
        }
        else if (prInherent == 5, srInherent == 5){
            print("Low");
        }
        else if (prInherent == 5, srInherent == 6){
            print("Medium");
        }
        else if (prInherent == 5, srInherent == 7){
            print("High");
        }
        else if (prInherent == 5, srInherent > 7){
            print("Very High");
        }
        else if (prInherent == 6, srInherent < 5){
            print("Medium");
        }
        else if (prInherent == 6, srInherent == 5){
            print("Medium");
        }
        else if (prInherent == 6, srInherent == 6){
            print("Medium");
        }
        else if (prInherent == 6, srInherent == 7){
            print("High");
        }
        else if (prInherent == 6, srInherent > 7){
            print("Very High");
        }
        else if (prInherent == 7, srInherent < 5){
            print("High");
        }
        else if (prInherent == 7, srInherent == 5){
            print("High");
        }
        else if (prInherent == 7, srInherent == 6){
            print("High");
        }
        else if (prInherent == 7, srInherent == 7){
            print("High");
        }
        else if (prInherent == 7, srInherent > 7){
            print("Very High");
        }
        else if (prInherent > 7, srInherent < 5){
            print("Very High");
        }
        else if (prInherent > 7, srInherent == 5){
            print("Very High");
        }
        else if (prInherent > 7, srInherent == 6){
            print("Very High");
        }
        else if (prInherent > 7, srInherent == 7){
            print("Very High");
        }
        else if (prInherent > 7, srInherent > 7){
            print("Very High")
        }
        else;{
            print("undefined");
        }
    }
}
);