const semicircles = document.querySelectorAll('.semicircle');
const timer = document.querySelector('.timer');


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
    const hrs = Math.floor(remainingTime / 3600000).toString().padStart(2, '0') ;
    const mins = Math.floor((remainingTime % 3600000) / 60000).toString().padStart(2, '0');
    const secs = Math.floor((remainingTime % 60000) / 1000).toString().padStart(2, '0'); 

    // const hrs = Math.floor(remainingTime / (1000 * 60 * 60) % 24).toString().padStart(2, '0') ;
    // const mins = Math.floor(remainingTime / (1000 * 60) % 60).toString().padStart(2, '0');
    // const secs = Math.floor((remainingTime / 1000) % 60).toString().padStart(2, '0');

    timer.innerHTML = `${hrs}:${mins}:${secs}`;

    // 5 second warning
    if (remainingTime <= 6000) {
        timer.style.color = `red`;
        semicircles[0].style.backgroundColor = `red`;
        semicircles[1].style.backgroundColor = `red`;
    }
    

    // end
    if (remainingTime <= 0) {
        clearInterval(timerLoop);

        semicircles[0].style.display = `none`;
        semicircles[1].style.display = `none`;
        semicircles[2].style.display = `none`;

        timer.innerHTML = `TIMES UP!`;

        timer.style.color = `gray`;
        return;
    }
}