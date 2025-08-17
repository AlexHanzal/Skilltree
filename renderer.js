const { ipcRenderer } = require('electron');

const achievmentbuttons = document.querySelectorAll('.achievement-button');
const achievementbuttonunlock = document.querySelectorAll('.achievement-button-unlock');
const achievementbuttonlock = document.querySelectorAll('.achievement-button-lock');

achievmentbuttons.forEach(button => {
    button.addEventListener('click', () => {
        // Hide all descriptions
        document.querySelectorAll('.achievement-description').forEach(desc => {
            desc.classList.add('hidden');
        });

        // Show only the description immediately after the clicked button
        const achievementdescription = button.nextElementSibling;
        if (achievementdescription && achievementdescription.classList.contains('achievement-description')) {
            const isVisible = !achievementdescription.classList.contains('hidden');
            if (!isVisible) {
                achievementdescription.classList.remove('hidden');
            }
        }
    });
});

achievementbuttonunlock.forEach(unlockBtn => {
    unlockBtn.addEventListener('click', (e) => {
        e.stopPropagation(); // Prevent triggering parent button click
        // Find the related achievement button (the previous sibling of the description)
        const achievementDescription = unlockBtn.closest('.achievement-description');
        if (achievementDescription) {
            const achievementBtn = achievementDescription.previousElementSibling;
            if (achievementBtn && achievementBtn.classList.contains('achievement-button')) {
                achievementBtn.classList.remove('locked');
                achievementBtn.classList.add('unlocked');
                // Send unlock event to main process
                ipcRenderer.send('achievement-unlocked', {
                    id: achievementBtn.textContent.trim() // Use a unique id if available
                });
            }
        }
    });
});
achievementbuttonlock.forEach(lockBtn => {
    lockBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        const achievementDescription = lockBtn.closest('.achievement-description');
        if (achievementDescription) {
            const achievementBtn = achievementDescription.previousElementSibling;
            if (achievementBtn && achievementBtn.classList.contains('achievement-button')) {
                achievementBtn.classList.remove('unlocked');
                achievementBtn.classList.add('locked');
                // Send unlock event to main process
                ipcRenderer.send('achievement-locked', {
                    id: achievementBtn.textContent.trim() // Use a unique id if available
                });
            }
        }
    });
});

// Request unlocked achievements on load
window.addEventListener('DOMContentLoaded', () => {
    ipcRenderer.invoke('get-unlocked-achievements').then(unlocked => {
        if (Array.isArray(unlocked)) {
            document.querySelectorAll('.achievement-button').forEach(btn => {
                const id = btn.textContent.trim();
                if (unlocked.includes(id)) {
                    btn.classList.remove('locked');
                    btn.classList.add('unlocked');
                } else {
                    btn.classList.remove('unlocked');
                    btn.classList.add('locked');
                }
            });
        }
    });
});
