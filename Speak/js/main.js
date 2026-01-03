const text = document.querySelector("input")
const btn = document.querySelector("button")
const speak = () => {
console.log(text.value)

    const utterance = new SpeechSynthesisUtterance(text.value)

    utterance.lang = "en-US";
    utterance.rate = 1;
    utterance.pitch = 2;

    speechSynthesis.speak(utterance);
}

btn.addEventListener("click",() => {
    speak()
})