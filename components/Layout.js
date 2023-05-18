import Sidebar from './Sidebar';
import { useContext } from 'react';
import { MyContext } from '@/AppStateProvider';

function Layout({ children }) {
	const { isActive, setIsActive } = useContext(MyContext);

	return (
		<div
			className='flex min-h-screen flex-col items-center 
        justify-between p-24 relative w-full overflow-hidden bg-white'
		>
			<Sidebar />

			<div
				className={`absolute h-full transition-all duration-500 ease-in-out p-10 z-10
                ${
									isActive
										? 'left-[240px] w-calc(100% - 240px)'
										: 'left-[78px] w-calc(100% - 78px)'
								}`}
			>
				{children}
			</div>
		</div>
	);
}

export default Layout;
