// Main JavaScript for Thyroid Prediction Website

document.addEventListener('DOMContentLoaded', function() {
    // Header scroll effect
    const header = document.querySelector('header');
    const navLinks = document.querySelectorAll('.nav-link');
    const mobileNavToggle = document.querySelector('.mobile-nav-toggle');
    const navMenu = document.querySelector('.nav-menu');
    
    // Scroll effect for header
    if (header) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });
    }
    
    // Mobile navigation toggle
    if (mobileNavToggle && navMenu) {
        mobileNavToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            mobileNavToggle.setAttribute('aria-expanded', 
                mobileNavToggle.getAttribute('aria-expanded') === 'true' ? 'false' : 'true'
            );
        });
    }
    
    // Form validation
    const predictionForm = document.getElementById('prediction-form');
    if (predictionForm) {
        predictionForm.addEventListener('submit', function(e) {
            let isValid = true;
            
            // Validate age
            const ageInput = document.getElementById('age');
            if (ageInput && (isNaN(ageInput.value) || ageInput.value < 18 || ageInput.value > 100)) {
                showError(ageInput, 'Please enter a valid age between 18 and 100');
                isValid = false;
            } else if (ageInput) {
                clearError(ageInput);
            }
            
            // Validate TSH
            const tshInput = document.getElementById('tsh');
            if (tshInput && (isNaN(tshInput.value) || tshInput.value <= 0 || tshInput.value > 20)) {
                showError(tshInput, 'Please enter a valid TSH value between 0 and 20');
                isValid = false;
            } else if (tshInput) {
                clearError(tshInput);
            }
            
            // Validate T3
            const t3Input = document.getElementById('t3');
            if (t3Input && (isNaN(t3Input.value) || t3Input.value <= 0 || t3Input.value > 400)) {
                showError(t3Input, 'Please enter a valid T3 value between 0 and 400');
                isValid = false;
            } else if (t3Input) {
                clearError(t3Input);
            }
            
            // Validate T4
            const t4Input = document.getElementById('t4');
            if (t4Input && (isNaN(t4Input.value) || t4Input.value <= 0 || t4Input.value > 25)) {
                showError(t4Input, 'Please enter a valid T4 value between 0 and 25');
                isValid = false;
            } else if (t4Input) {
                clearError(t4Input);
            }
            
            if (!isValid) {
                e.preventDefault();
            }
        });
    }
    
    // Results page animations
    const resultBox = document.querySelector('.result-box');
    if (resultBox) {
        resultBox.classList.add('animate-fade-in');
        
        // Animate probability bars
        const probabilityFills = document.querySelectorAll('.probability-fill');
        setTimeout(() => {
            probabilityFills.forEach(fill => {
                const width = fill.getAttribute('data-width');
                fill.style.width = width + '%';
            });
        }, 300);
    }
    
    // Tooltip initialization
    initTooltips();
    
    // Information toggles
    const infoToggleBtns = document.querySelectorAll('.info-toggle');
    infoToggleBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const targetId = this.getAttribute('data-target');
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                targetElement.classList.toggle('hidden');
                
                // Change the button text/icon
                const isExpanded = this.getAttribute('aria-expanded') === 'true';
                this.setAttribute('aria-expanded', !isExpanded);
                
                // If we're using an icon, we would toggle classes here
                // this.querySelector('svg').classList.toggle('rotate-180');
                
                // If it's text, we might change the content
                if (this.textContent.includes('Show')) {
                    this.textContent = this.textContent.replace('Show', 'Hide');
                } else {
                    this.textContent = this.textContent.replace('Hide', 'Show');
                }
            }
        });
    });
});

// Helper functions
function showError(input, message) {
    const formGroup = input.closest('.form-group');
    const errorElement = formGroup.querySelector('.error-message') || document.createElement('div');
    
    errorElement.className = 'error-message';
    errorElement.style.color = 'var(--error)';
    errorElement.style.fontSize = 'var(--font-sm)';
    errorElement.style.marginTop = 'var(--space-xs)';
    errorElement.textContent = message;
    
    if (!formGroup.querySelector('.error-message')) {
        input.parentNode.appendChild(errorElement);
    }
    
    input.style.borderColor = 'var(--error)';
    input.classList.add('is-invalid');
}

function clearError(input) {
    const formGroup = input.closest('.form-group');
    const errorElement = formGroup.querySelector('.error-message');
    
    if (errorElement) {
        errorElement.remove();
    }
    
    input.style.borderColor = '';
    input.classList.remove('is-invalid');
}

function initTooltips() {
    const tooltips = document.querySelectorAll('[data-tooltip]');
    
    tooltips.forEach(tooltip => {
        tooltip.addEventListener('mouseenter', function() {
            const tooltipText = this.getAttribute('data-tooltip');
            const tooltipElement = document.createElement('div');
            
            tooltipElement.className = 'tooltip';
            tooltipElement.textContent = tooltipText;
            tooltipElement.style.position = 'absolute';
            tooltipElement.style.backgroundColor = 'var(--text-dark)';
            tooltipElement.style.color = 'white';
            tooltipElement.style.padding = 'var(--space-sm) var(--space-md)';
            tooltipElement.style.borderRadius = 'var(--border-radius-sm)';
            tooltipElement.style.fontSize = 'var(--font-sm)';
            tooltipElement.style.zIndex = '1000';
            tooltipElement.style.pointerEvents = 'none';
            tooltipElement.style.opacity = '0';
            tooltipElement.style.transition = 'opacity 200ms ease';
            
            document.body.appendChild(tooltipElement);
            
            const rect = this.getBoundingClientRect();
            const tooltipRect = tooltipElement.getBoundingClientRect();
            
            tooltipElement.style.top = (rect.top - tooltipRect.height - 10) + 'px';
            tooltipElement.style.left = (rect.left + (rect.width / 2) - (tooltipRect.width / 2)) + 'px';
            
            setTimeout(() => {
                tooltipElement.style.opacity = '1';
            }, 10);
            
            this.addEventListener('mouseleave', function onMouseLeave() {
                tooltipElement.style.opacity = '0';
                
                setTimeout(() => {
                    document.body.removeChild(tooltipElement);
                }, 200);
                
                this.removeEventListener('mouseleave', onMouseLeave);
            });
        });
    });
}

// API functions for advanced usage
async function predictViaAPI(data) {
    try {
        const response = await fetch('/api/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });
        
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        
        return await response.json();
    } catch (error) {
        console.error('Error predicting via API:', error);
        throw error;
    }
}

// Chart initialization (if using charts for results)
function initResultsChart(normalProb, hypoProb, hyperProb) {
    const ctx = document.getElementById('results-chart');
    
    if (ctx && window.Chart) {
        new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ['Normal', 'Hypothyroidism', 'Hyperthyroidism'],
                datasets: [{
                    data: [normalProb, hypoProb, hyperProb],
                    backgroundColor: [
                        'var(--success)',
                        'var(--warning)',
                        'var(--error)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                cutout: '70%',
                plugins: {
                    legend: {
                        position: 'bottom'
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return context.label + ': ' + context.raw + '%';
                            }
                        }
                    }
                }
            }
        });
    }
}