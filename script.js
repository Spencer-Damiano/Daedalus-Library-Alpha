const semicircles = document.querySelectorAll('.semicircle');


//input
const hr = 0;
const min = 0;
const sec = 10;

const hours = hr * 3600000;
const minutes = min * 60000;
const seconds = sec * 1000;
const setTime = hours + minutes + seconds;
const startTime = Date.now();
const futureTime = startTime + setTime;

const timerLoop = setInterval(countDownTimer);
countDownTimer();

function countDownTimer() {

    const currentTime = Date.now();
    const remainingTime = futureTime - currentTime;
    const angle = remainingTime / setTime * 360;

    // progress indicator

    if(angle > 180){
        semicircles[2].style.display = `none`;
        semicircles[0].style.transform = `rotate(180deg)`;
        semicircles[1].style.transform = `rotate(${angle}deg)`;
    } else {
        semicircles[2].style.display = `block`;
        semicircles[0].style.transform = `rotate(${angle}deg)`;
        semicircles[1].style.transform = `rotate(${angle}deg)`;
    }



    //timer

    // 5 second warning

    

    // end
    if (remainingTime <= 0) {
        clearInterval(timerLoop);
        return;
    }
}