$(document).ready(function(){

    // FUNCTION TO FETCH THE DATA FROM DATABASE.
    function getData(ID){

        $(".custom-control-input").val("");

        url = "http://127.0.0.1:8000/exam/multiplechoiceapi/"+ID;
        fetch(url).then((response)=>{
            return response.json();
        }).then((data)=>{
            // console.log(data)
            $("#multiple-choice-question").text(data["id"]+". "+data["question"]);
            $("#radio1").text(data["option1"]);
            $("#radio2").text(data["option2"]);
            $("#radio3").text(data["option3"]);
            $("#radio4").text(data["option4"]);
        });
    }

    // LOAD THE FIRST QUESTION WHEN PAGE IS LOADED.
    getData(1);
    
    function postData(ID, submittedAnswer){
        url = "http://127.0.0.1:8000/exam/multiplechoiceapi/"+ID;
        data = "{'submitted_answer':"+submittedAnswer+"}"
        params = {
            method:'post',
            headers: {
                'Content-Type': 'application/json'
            },
            body: data
        }
        fetch(url, params).then(response=> response.json())
        .then(data => console.log(data)
        )
    }
    
    // console.log("Before running getData")
    // getData()
    // console.log("After running getData")
    // postData()
    $("#submitm").click(function(){

        let submittedAnswer = $("input[name='radio-stacked']:checked").attr('id');
        if(submittedAnswer){
            var ID = $("#multiple-choice-question").text()[0];
            postData(ID, submittedAnswer);
            getData(Number(ID)+1);

            $("#"+submittedAnswer).prop("checked", false);
        }else{
            alert("Please choose the optoin.");
        }
    });

    $("#prevm").click(function(){

        getData(ID-1);

    });
    $("#prevm").click(function(){

        getData(ID+1);

    });
    
    $("#login").click(function(){
        $(".login").hide()
    })

    $("#signup").click(function(){
        $(".login").show()
    })
});
