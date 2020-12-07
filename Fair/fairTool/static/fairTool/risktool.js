$(document).ready(function(){
    var col_list = ["rgb(0, 128, 6)","rgb(76, 187, 82)", "rgb(244, 255, 85)", "rgb(255, 52, 52)", "rgb(255, 0, 0)"];
    function set_color(_color, _id){
        $("#" + _id).animate().css({
            backgroundColor: _color
        }, 2500);
    }
    
    function setnum1(_a, _b, _id){
        var _sum = parseInt(_a) + parseInt(_b);
        var ans;
        if(_sum < 5){
            ans = 1;
        }
        else if(_sum > 7){
            ans = 5;
        }
        else{
            ans = _sum-3;
        }
        settext(ans, _id);
        set_color(col_list[ans-1], _id);

        return ans;
    }

    function lef(_a, _b, _id){
        var tab = [
            [1,1,1,1,1],
            [1,1,2,2,2],
            [1,2,3,3,3],
            [2,3,4,4,4],
            [3,4,5,5,5]
        ];
        var x = parseInt(_a) - 1;
        var y = parseInt(_b) - 1;
        var ans = tab[x][y];
        settext(ans, _id);
        set_color(col_list[ans-1], _id);
        return ans;
    }

    function vun(_a, _b, _id){
        var tab = [
            [3,2,1,1,1],
            [4,3,2,1,1],
            [5,4,3,2,1],
            [5,5,4,3,2],
            [5,5,5,4,3]
        ];
        var x = parseInt(_a) - 1;
        var y = parseInt(_b) - 1;
        var ans = tab[x][y];
        settext(ans, _id);
        set_color(col_list[ans-1], _id);
        return ans;
    }

    function settext(_val,_id){
        $("#" + _id).val(_val);
    }

    function ova(_a,_b,_id){
        var x = parseInt(_a);
        var y = parseInt(_b);
        var val = Math.max(x,y);
        settext(val, _id);
        set_color(col_list[val-1], _id);
        return val;
    }

    $("#submit").click(function(){
        const outputs = {"ori-01":0, "orr-01":0, "pri-01":0, "prr-01":0, "plefi-01":0, "plefr-01":0, "tefi-01":0, "tefr-01":0, "vi-01":0, "vr-01":0, "sri-01":0, "srr-01":0, "slefi-01":0, "slefr-01":0};
       
        outputs["tefi-01"] = setnum1($("select[name=poadi]").val(),$("select[name=cfai]").val(), "tefi-01");
        outputs["tefr-01"] = setnum1($("select[name=poadr]").val(),$("select[name=cfar]").val(), "tefr-01");

        outputs["vi-01"] = vun($("select[name=tcp]").val(),$("select[name=rsvi]").val(), "vi-01");
        outputs["vr-01"] = vun($("select[name=tcp]").val(),$("select[name=rsvr]").val(), "vr-01");

        outputs["plefi-01"] = lef($("#vi-01").val(),$("#tefi-01").val(), "plefi-01");
        outputs["plefr-01"] = lef($("#tefr-01").val(), $("#vr-01").val(), "plefr-01");
        outputs["plefi-02"] = lef($("#vi-01").val(),$("#tefi-01").val(), "plefi-02");
        outputs["plefr-02"] = lef($("#tefr-01").val(), $("#vr-01").val(), "plefr-02");

        outputs["slefi-01"] = setnum1($("#plefi-02").val(), $("select[name=slp]").val(), "slefi-01");
        outputs["slefr-01"] = setnum1($("#plefr-02").val(), $("select[name=slp]").val(), "slefr-01");

        outputs["pri-01"] = setnum1($("#plefi-01").val(),$("select[name=plmi]").val(), "pri-01");
        outputs["prr-01"] = setnum1($("#plefi-01").val(),$("select[name=plmr]").val(), "prr-01");

        outputs["sri-01"] = setnum1($("#slefi-01").val(),$("select[name=slmri]").val(), "sri-01");
        outputs["srr-01"] = setnum1($("#slefr-01").val(),$("select[name=slmrr]").val(), "srr-01");

        outputs["ori-01"] = ova($("#pri-01").val(), $("#prr-01").val(), "ori-01");
        outputs["orr-01"] = ova($("#prr-01").val(), $("#prr-01").val(), "orr-01");
    });
});