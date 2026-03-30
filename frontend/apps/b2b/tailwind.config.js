import frappeUIPreset from 'frappe-ui/src/tailwind/preset'
export default {
	darkMode: 'class',
	presets: [frappeUIPreset],
	content: [
		'./index.html',
		'./src/**/*.{vue,js,ts,jsx,tsx}',
		'./node_modules/frappe-ui/src/components/**/*.{vue,js,ts,jsx,tsx}',
		'../node_modules/frappe-ui/src/components/**/*.{vue,js,ts,jsx,tsx}',
	],
	theme: {
		extend: {
			fontFamily: {
				sans: ['Outfit', 'Inter', 'system-ui', 'sans-serif'],
			},
			colors: {
				brand: {
					primary: '#059669',     // Emerald 600 — main brand
					'primary-light': '#34d399', // Emerald 400
					'primary-dark': '#047857',  // Emerald 700
					secondary: '#0891b2',   // Cyan 600
					'secondary-light': '#22d3ee', // Cyan 400
					accent: '#f43f5e',      // Rose 500 — CTA / alerts
					'accent-warm': '#f97316', // Orange 500
					dark: '#0a0f1a',        // Deep navy
					surface: '#f0fdf4',     // Emerald 50 — light bg tint
				}
			},
			boxShadow: {
				'glass': '0 8px 32px 0 rgba(5, 150, 105, 0.08)',
				'glass-strong': '0 12px 48px 0 rgba(5, 150, 105, 0.15)',
				'neon': '0 0 20px rgba(5, 150, 105, 0.4), 0 0 40px rgba(5, 150, 105, 0.1)',
				'neon-accent': '0 0 20px rgba(244, 63, 94, 0.4)',
				'float': '0 20px 60px rgba(0, 0, 0, 0.08), 0 8px 20px rgba(0, 0, 0, 0.04)',
				'inner-glow': 'inset 0 1px 4px 0 rgba(5, 150, 105, 0.06)',
			},
			animation: {
				'float': 'float 4s ease-in-out infinite',
				'float-slow': 'float 6s ease-in-out infinite',
				'pulse-subtle': 'pulseSubtle 2.5s cubic-bezier(0.4, 0, 0.6, 1) infinite',
				'fade-in-up': 'fadeInUp 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards',
				'fade-in-down': 'fadeInDown 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards',
				'fade-in': 'fadeIn 0.4s ease-out forwards',
				'slide-up': 'slideUp 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards',
				'slide-down': 'slideDown 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards',
				'scale-in': 'scaleIn 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards',
				'shimmer': 'shimmer 2s infinite linear',
				'spin-slow': 'spin 3s linear infinite',
				'bounce-subtle': 'bounceSoft 1s ease-in-out infinite',
				'morph': 'morph 8s ease-in-out infinite',
				'glow-pulse': 'glowPulse 2s ease-in-out infinite',
			},
			keyframes: {
				float: {
					'0%, 100%': { transform: 'translateY(0)' },
					'50%': { transform: 'translateY(-8px)' },
				},
				pulseSubtle: {
					'0%, 100%': { opacity: '1' },
					'50%': { opacity: '0.7' },
				},
				fadeInUp: {
					'0%': { opacity: '0', transform: 'translateY(16px)' },
					'100%': { opacity: '1', transform: 'translateY(0)' },
				},
				fadeInDown: {
					'0%': { opacity: '0', transform: 'translateY(-16px)' },
					'100%': { opacity: '1', transform: 'translateY(0)' },
				},
				fadeIn: {
					'0%': { opacity: '0' },
					'100%': { opacity: '1' },
				},
				slideUp: {
					'0%': { opacity: '0', transform: 'translateY(100%)' },
					'100%': { opacity: '1', transform: 'translateY(0)' },
				},
				slideDown: {
					'0%': { opacity: '0', transform: 'translateY(-20px)' },
					'100%': { opacity: '1', transform: 'translateY(0)' },
				},
				scaleIn: {
					'0%': { opacity: '0', transform: 'scale(0.9)' },
					'100%': { opacity: '1', transform: 'scale(1)' },
				},
				shimmer: {
					'0%': { backgroundPosition: '-200% 0' },
					'100%': { backgroundPosition: '200% 0' },
				},
				bounceSoft: {
					'0%, 100%': { transform: 'translateY(0)' },
					'50%': { transform: 'translateY(-4px)' },
				},
				morph: {
					'0%, 100%': { borderRadius: '60% 40% 30% 70% / 60% 30% 70% 40%' },
					'25%': { borderRadius: '30% 60% 70% 40% / 50% 60% 30% 60%' },
					'50%': { borderRadius: '50% 60% 30% 60% / 30% 60% 70% 40%' },
					'75%': { borderRadius: '60% 40% 60% 30% / 40% 50% 60% 50%' },
				},
				glowPulse: {
					'0%, 100%': { boxShadow: '0 0 20px rgba(5, 150, 105, 0.3)' },
					'50%': { boxShadow: '0 0 40px rgba(5, 150, 105, 0.6), 0 0 80px rgba(5, 150, 105, 0.2)' },
				},
			},
			screens: {
				standalone: {
					raw: '(display-mode: standalone)',
				},
			},
			padding: {
				'safe-top': 'env(safe-area-inset-top)',
				'safe-right': 'env(safe-area-inset-right)',
				'safe-bottom': 'env(safe-area-inset-bottom)',
				'safe-left': 'env(safe-area-inset-left)',
			},
			backdropBlur: {
				'xl': '24px',
				'2xl': '40px',
				'3xl': '64px',
			},
			borderRadius: {
				'4xl': '2rem',
				'5xl': '2.5rem',
			},
		},
	},
	corePlugins: {
		aspectRatio: false,
	},
	plugins: [require('@tailwindcss/aspect-ratio')],
}
