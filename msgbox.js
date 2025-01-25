document.addEventListener("DOMContentLoaded", () => {
    const messages = [
        "Sabias que o diploma tem o mesmo valor entre os Politécnicos e as Universidades?",
        "Tens de escolher a instituição que mais se adapta aos teus objetivos!",
        "Politécnicos focam na prática; Universidades, na teoria!",
        "Ambas as opções formam profissionais competentes!",
        "Pesquisa sobre os cursos antes de tomar uma decisão!"
    ];

    const messageBox = document.createElement("div");
    messageBox.id = "messageBox";
    messageBox.textContent = getRandomMessage();

    document.body.prepend(messageBox);

    setInterval(() => {
        messageBox.textContent = getRandomMessage();
    }, 5000);

    function getRandomMessage() {
        return messages[Math.floor(Math.random() * messages.length)];
    }
});
