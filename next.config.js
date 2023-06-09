/** @type {import('next').NextConfig} */
const nextConfig = {
	reactStrictMode: true,
	swcMinify: true,
	async rewrites() {
		return [
			{
				source: '/loginS/:path*',
				destination: 'http://localhost:8086/:path*',
			},
		];
	},
};

module.exports = nextConfig;
