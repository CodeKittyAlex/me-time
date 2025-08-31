let speed = 500;
const height = 20;
const width = 20;

const up = [-1, 0]
const down = [1, 0]
const left = [0, -1]
const right = [0, 1]

let direction = right
let apple = null
let snake= [[3, 2], [3, 3], [3, 4], [3, 5]]
const playboard = document.getElementById("playboard");
let grid = [];

// Loo mänguala
for (let y = 0; y < height; y++) {
    let row= document.createElement("tr")
    let thlist = [];
    for (let x = 0; x < width; x++) {
        let col= document.createElement("th")
        row.appendChild(col);
        thlist.push(col)
    }
    grid.push( thlist );
    playboard.appendChild(row);
}

// Lisa ussi ruudud
function render () {
    grid.forEach(function (gridrow){
       gridrow.forEach(function (gridsquare){
        gridsquare.classList.remove("snake");
        gridsquare.classList.remove("apple");
       })
    })
        let x = apple[1]
        let y = apple[0]
        grid[y][x].classList.add("apple");
    snake.forEach(function (snakecord) {
        let x = snakecord[1]
        let y = snakecord[0]
        try{
            grid[y][x].classList.add("snake");
        }catch(err){
            clearInterval(game)
        }
    }
)}
function applepos (){
    let applex = Math.floor(Math.random() * height);
    let appley = Math.floor(Math.random() * width);
    let applesum = [appley, applex]
    return applesum
}
    let appledub = applepos()
    apple = appledub

    let bodyend = snake.at(0)
    //console.log(bodyend)
    //snake.push(bodyend)

game = setInterval(function() {
    //console.log(snake)
    let snakehead = snake.at(-1)
    //console.log(apple)
    //console.log(snakehead)

    if (apple[0] == snakehead[0] && apple[1] == snakehead[1]){
        //console.log("+punkt")
        applepos()
        let appledub = applepos()
        let bodyend = snake.at(0)
        apple = appledub
        //console.log(bodyend)
        snake.unshift(bodyend)
    }
    //console.log(snake)
    snake.shift()
    let newhead_x = snakehead[1] + direction[1]
    let newhead_y = snakehead[0] + direction[0]
    let subList =([newhead_y, newhead_x])
    function containsSimilarList(snake, subList) {
    for (let i = 0; i < snake.length; i++) {
        const currentList = snake[i];
        if (currentList.length === subList.length) {
            let similar = true;
            for (let j = 0; j < subList.length; j++) {
                if (currentList[j] !== subList[j]) {
                    similar = false;
                    break;
                }
            }
            if (similar) {
                return true;
            }
        }
    }
    return false;
}
if(containsSimilarList(snake, subList) == true) {
    clearInterval(game)
}
//console.log(containsSimilarList(snake, subList));
    snake.push([newhead_y, newhead_x])
    render()

}, speed);

document.addEventListener('keydown', function(event) {
//console.log(event.keyCode)
    if (event.keyCode == 39 && direction != left) {
        direction = right
    }
    if (event.keyCode == 38 && direction != down) {
        direction = up
    }
    if (event.keyCode == 37 && direction != right) {
         direction = left
    }
    if (event.keyCode == 40 && direction != up) {
            direction = down
    }
})



