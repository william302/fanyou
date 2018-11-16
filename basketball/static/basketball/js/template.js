window.onload = function(){

    var color= "#f00";
    $(".table").css("background",color);
    $(".search input").css("border-color",color);
    $(".pank h2,.search button,.voteDetail .voteBtn,.confrim").css("background",color);

   
    // 显示报名
    $(".signBtn").click(function(){
         // $(".mask,.return").removeClass('hide');
         // $(".container,.detail,.admin,.list").addClass('hide');
        window.location.href = '/basketball/';
    })

    var activiy = true;
    // 显示活动详情
    $(".activtyBtn").click(function(){

        if(activiy===true){
         $(".detail,.return").removeClass('hide');
         $(".container, .displayPic").addClass('hide');
         activiy = false;
        }
        else {
         $(".detail,.return").addClass('hide');
         $(".container, .displayPic").removeClass('hide');
         activiy = true;
        }
    })


    // 显示我的

    $(".adminBtn").click(function(){
        $(".admin,.return").removeClass('hide');
         $(".container,.mask,.detail,.list,.displayPic").addClass('hide');
    })

    // 点击返回，返回主页
    $(".return").click(function(){
        $(".container").removeClass('hide');
         window.location.reload();
        $(".signBtn,.mask,.detail,.return,.list,.displayPic").addClass('hide');
    })

    // 点击查看排名
    $(".pank").click(function(event) {
        $(".return,.list").removeClass('hide');
        $(".signBtn,.mask,.detail,.container,.displayPic").addClass('hide');
    });
    
    // 点击确认报名
    $(".confrim").click(function(event) {
        $(this).attr("disabled", true);
    });

};