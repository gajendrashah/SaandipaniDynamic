        const text = document.getElementById('dancing-text');
        
        function dance() {
            const animations = [
                'translateY(-20px)',
                'translateX(10px)', 
                'translateY(20px)',
                'translateX(-10px)'
            ];
            let i = 0;
            
            setInterval(() => {
                text.style.transform = animations[i];
                i = (i + 1) % animations.length;
            }, 500);
        }

        window.onload = dance;