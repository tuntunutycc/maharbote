document.addEventListener('DOMContentLoaded', () => {
    const birthDaySelect = document.getElementById('birthDay');
    const aspectSelect = document.getElementById('aspect');
    const getFortuneBtn = document.getElementById('getFortune');
    const fortuneResult = document.getElementById('fortuneResult');
    const predictionText = document.getElementById('prediction');

    getFortuneBtn.addEventListener('click', async () => {
        const day = birthDaySelect.value;
        const aspect = aspectSelect.value;

        if (!day || !aspect) {
            alert('Please select both your birth day and the aspect of life you want to know about.');
            return;
        }

        try {
            getFortuneBtn.disabled = true;
            getFortuneBtn.textContent = 'Getting your fortune...';

            const response = await fetch('/fortune', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ day, aspect }),
            });

            if (!response.ok) {
                throw new Error('Failed to get fortune');
            }

            const data = await response.json();
            
            // Add a fade-in effect
            fortuneResult.style.opacity = '0';
            predictionText.textContent = data.prediction;
            fortuneResult.style.display = 'flex';
            
            // Trigger reflow
            fortuneResult.offsetHeight;
            
            // Add fade-in animation
            fortuneResult.style.transition = 'opacity 0.5s ease-in-out';
            fortuneResult.style.opacity = '1';

        } catch (error) {
            predictionText.textContent = 'Sorry, there was an error getting your fortune. Please try again.';
            console.error('Error:', error);
        } finally {
            getFortuneBtn.disabled = false;
            getFortuneBtn.textContent = 'Get Your Fortune';
        }
    });
}); 