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
			colors: {
				brand: {
					primary: '#8b5cf6',
					secondary: '#06b6d4',
					accent: '#f43f5e',
					dark: '#0f172a',
				}
			},
			boxShadow: {
				'glass': '0 8px 32px 0 rgba(31, 38, 135, 0.07)',
				'neon': '0 0 15px rgba(139, 92, 246, 0.5)',
			},
			animation: {
				'float': 'float 3s ease-in-out infinite',
				'pulse-subtle': 'pulseSubtle 2s cubic-bezier(0.4, 0, 0.6, 1) infinite',
				'fade-in-up': 'fadeInUp 0.5s ease-out forwards',
			},
			keyframes: {
				float: {
					'0%, 100%': { transform: 'translateY(0)' },
					'50%': { transform: 'translateY(-5px)' },
				},
				pulseSubtle: {
					'0%, 100%': { opacity: '1' },
					'50%': { opacity: '0.8' },
				},
				fadeInUp: {
					'0%': { opacity: '0', transform: 'translateY(10px)' },
					'100%': { opacity: '1', transform: 'translateY(0)' },
				}
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
		},
	},
	corePlugins: {
		aspectRatio: false,
	},
	plugins: [require('@tailwindcss/aspect-ratio')],
}
