// Wait for the DOM content to be fully loaded before executing the script.
document.addEventListener('DOMContentLoaded', function() {
  // Get references to various elements in the HTML document.
  const exerciseButtons = document.querySelectorAll('.exercise-button');
  const exerciseModal = document.getElementById('exerciseModal222');
  const exerciseTitleElement = exerciseModal.querySelector('.exercise-title');
  const circle = document.getElementById("circle");
  const timer = document.getElementById("timer");
  const cycleCounter = document.getElementById('cycle-counter');
  const startButton = document.getElementById("start");
  const stopButton = document.getElementById("stop");
  const circletext = document.getElementById("circletext");

  // Initialize variables for animation control and timing.
  let isAnimating = false;
  let animationId = null;
  let currentCycle = 0;
  let currentPhase = "IN";
  let phaseStartTime = null;
  let totalCycles = 0;
  let inDuration = 0;
  let holdDuration = 0;
  let outDuration = 0;

  // Add an event listener to hide the exercise modal and stop the animation when the modal is hidden.
  exerciseModal.addEventListener('hidden.bs.modal', function () {
    const backdrop = document.querySelector('.modal-backdrop');
    if (backdrop) {
        backdrop.remove();
    }
    stopAnimation();
  });

  // Add click event listeners to exercise buttons.
  exerciseButtons.forEach(function(button) {
    button.addEventListener('click', function(event) {
      const clickedButton = event.currentTarget;
      // Extract the exercise information from data attributes of the clicked button.
      const exerciseTitle = clickedButton.getAttribute('data-exercise-title');
      inDuration = parseInt(clickedButton.getAttribute('data-exercise-in')); // seconds
      holdDuration = parseInt(clickedButton.getAttribute('data-exercise-hold')); // seconds
      outDuration = parseInt(clickedButton.getAttribute('data-exercise-out')); // seconds
      totalCycles = parseInt(clickedButton.getAttribute('data-exercise-cycles')); // Set the desired number of cycles

      // Update the exercise title in the modal.
      exerciseTitleElement.textContent = 'Exercise: ' + exerciseTitle;

      // Reset the currentCycle to 0.
      currentCycle = 0;
    });
  });

  // Add click event listeners to start and stop buttons.
  startButton.addEventListener("click", startAnimation);
  stopButton.addEventListener("click", stopAnimation);

  // Function to start the animation.
  function startAnimation() {
    if (!isAnimating) {
      isAnimating = true;
      currentCycle = 0;
      currentPhase = "OUT"; // Set the initial phase to "OUT"
      phaseStartTime = null;
      updateCycleCounter();
      animateCircle();
    }
  }

  // Function to perform the circle animation.
  function animateCircle(timestamp) {
    if (!phaseStartTime) {
      phaseStartTime = timestamp;
    }

    let elapsed = timestamp - phaseStartTime;

    if (currentPhase === "IN") {
      if (elapsed < inDuration * 1000) {
        // Ease-in effect to increase the circle size.
        let progress = elapsed / (inDuration * 1000);
        let easedProgress = Math.sin(progress * (Math.PI / 2));
        let newSize = 100 + easedProgress * (250 - 100);
        circle.style.width = newSize + "px";
        circle.style.height = newSize + "px";
        timer.innerText = "TIME: IN " + Math.ceil(elapsed / 1000) + "s";
        circletext.innerText = "IN";
      } else {
        // IN phase completed, move to HOLD phase.
        currentPhase = "HOLD";
        phaseStartTime = timestamp; // Reset the phase start time
        timer.innerText = "TIME: HOLD 0s"; // Reset timer for the HOLD phase
        circletext.innerText = "HOLD";
      }
    } else if (currentPhase === "HOLD") {
      if (elapsed < holdDuration * 1000) {
        // Hold the circle at its current size.
        circle.style.width = "250px";
        circle.style.height = "250px";
        timer.innerText = "TIME: HOLD " + Math.ceil(elapsed / 1000) + "s";
        circletext.innerText = "HOLD";
      } else {
        // HOLD phase completed, move to OUT phase.
        currentPhase = "OUT";
        phaseStartTime = timestamp; // Reset the phase start time
        timer.innerText = "TIME: OUT 0s"; // Reset timer for the OUT phase
        circletext.innerText = "OUT";
      }
    } else if (currentPhase === "OUT") {
      if (elapsed < outDuration * 1000) {
        // Ease-out effect to decrease the circle size.
        let progress = elapsed / (outDuration * 1000);
        let easedProgress = Math.sin(progress * (Math.PI / 2));
        let newSize = 250 - easedProgress * (250 - 100);
        circle.style.width = newSize + "px";
        circle.style.height = newSize + "px";
        timer.innerText = "TIME: OUT " + Math.ceil(elapsed / 1000) + "s";
        circletext.innerText = "OUT";
      } else {
        // OUT phase completed.
        currentPhase = ""; // Reset current phase
        phaseStartTime = null; // Reset phase start time
        currentCycle++;

        if (currentCycle === totalCycles + 1) {
          // All cycles completed, stop the animation.
          isAnimating = false;
          cycleCounter.innerText = "Cycle:";
          return;
        } else {
          // Start the next cycle by moving to the IN phase.
          currentPhase = "IN";
          phaseStartTime = timestamp; // Reset the phase start time
          updateCycleCounter();
        }
      }
    }

    // Continue the animation by requesting the next frame.
    animationId = requestAnimationFrame(animateCircle);
  }

  // Function to stop the animation.
  function stopAnimation() {
    cancelAnimationFrame(animationId);
    isAnimating = false;
    currentCycle = 0;
    currentPhase = "";
    phaseStartTime = null;
    circle.style.width = "100px";
    circle.style.height = "100px";
    timer.innerText = "TIME:";
    cycleCounter.innerText = "Cycle:";
  }

  // Function to update the cycle counter display.
  function updateCycleCounter() {
    cycleCounter.innerText = "Cycle: " + currentCycle + " of " + totalCycles;
  }
});
