import Image from 'next/image';
import { VscLink } from 'react-icons/vsc';
import { BiUser, BiMenu, BiLogOutCircle } from 'react-icons/bi';
import { BsFillPersonVcardFill } from 'react-icons/bs';
import { AiFillSchedule } from 'react-icons/ai';
import { FaUsers } from 'react-icons/fa';
import Link from 'next/link';
import { useContext } from 'react';
import { MyContext } from '@/AppStateProvider';

import { useState } from 'react';

function Sidebar() {
	const { isActive, setIsActive } = useContext(MyContext);

	const handleToggle = () => {
		setIsActive((isActive) => {
			return !isActive;
		});
	};

	return (
		<div
			className={`sidebar fixed top-0 left-0 h-full bg-primary-dark px-[14px] py-[6px]
		transition-all duration-500 ease-in-out ${isActive ? 'w-[240px]' : 'w-[78px]'}`}
		>
			<div className='logo_content'>
				<div
					className={`flex items-center h-[50px]
							pointer-events-none transition-all duration-500 ease-in-out 
							text-white ${isActive ? 'opacity-100' : 'opacity-0'}`}
				>
					<VscLink className='text-[28px] mr-[5px]' />
					<div className='text-[20px] font-normal'>Leekar</div>
				</div>
			</div>
			<BiMenu
				className={`absolute text-white top-[22px] text-[20px] h-[19px] w-[50px]
				text-center leading-[50px] -translate-x-[50%]
				${isActive ? 'left-[90%]' : 'left-[50%]'}`}
				onClick={handleToggle}
			/>

			<ul className='mt-[20px]'>
				<li className='group relative h-[50px] w-full my-0 list-none leading-[50px]'>
					<Link className='sidebar-link' href='/DoctorInfoPage'>
						<BiUser className='icon' />
						<span
							className={`transition-all duration-500 ease-in-out
						${
							isActive
								? 'opacity-1 pointer-events-auto'
								: 'opacity-0 pointer-events-none'
						}`}
						>
							Profile
						</span>
					</Link>
					<span
						className={`tooltip
						group-hover:transition-all group-hover:duration-500 group-hover:ease-in-out
						group-hover:opacity-100 group-hover:top-[50%]
						${isActive ? 'hidden' : 'block'}`}
					>
						Profile
					</span>
				</li>

				<li className='group relative h-[50px] w-full my-0 list-none leading-[50px]'>
					<Link className='sidebar-link' href='/'>
						<AiFillSchedule className='icon' />
						<span
							className={`transition-all duration-500 ease-in-out
						${
							isActive
								? 'opacity-1 pointer-events-auto'
								: 'opacity-0 pointer-events-none'
						}`}
						>
							Schedule
						</span>
					</Link>
					<span
						className={`tooltip
						group-hover:transition-all group-hover:duration-500 group-hover:ease-in-out
						group-hover:opacity-100 group-hover:top-[50%]
						${isActive ? 'hidden' : 'block'}`}
					>
						Schedule
					</span>
				</li>

				<li className='group relative h-[50px] w-full my-0 list-none leading-[50px]'>
					<a className='sidebar-link' href='#'>
						<BsFillPersonVcardFill className='icon' />
						<span
							className={`transition-all duration-500 ease-in-out
						${
							isActive
								? 'opacity-1 pointer-events-auto'
								: 'opacity-0 pointer-events-none'
						}`}
						>
							Health card
						</span>
					</a>
					<span
						className={`tooltip
						group-hover:transition-all group-hover:duration-500 group-hover:ease-in-out
						group-hover:opacity-100 group-hover:top-[50%]
						${isActive ? 'hidden' : 'block'}`}
					>
						Health card
					</span>
				</li>

				<li className='group relative h-[50px] w-full my-0 list-none leading-[50px]'>
					<a className='sidebar-link' href='#'>
						<FaUsers className='icon' />
						<span
							className={`transition-all duration-500 ease-in-out
						${
							isActive
								? 'opacity-1 pointer-events-auto'
								: 'opacity-0 pointer-events-none'
						}`}
						>
							Patients
						</span>
					</a>
					<span
						className={`tooltip
						group-hover:transition-all group-hover:duration-500 group-hover:ease-in-out
						group-hover:opacity-100 group-hover:top-[50%]
						${isActive ? 'hidden' : 'block'}`}
					>
						Patients
					</span>
				</li>
			</ul>

			<div className='absolute text-white bottom-0 left-0 w-full'>
				<div
					className={`relative px-[10px] py-[6px] h-[60px] bg-none
				transition-all duration-400 ease-in-out
				${isActive ? 'bg-primary' : ''}`}
				>
					<div
						className={` flex items-center whitespace-nowrap
						transition-all duration-500 ease-in-out
						${
							isActive
								? 'opacity-1 pointer-events-auto'
								: 'opacity-0 pointer-events-none'
						}`}
					>
						<Image
							className='h-[45px] w-[45px] object-cover rounded-xl'
							src='/profile.jpg'
							width={50}
							height={50}
							alt=''
						/>
						<div className='ml-[10px]'>
							<div className='text-[15px] font-normal'>Ilya Konsty</div>
							<div className='text-[12px]'>Doctor</div>
						</div>
					</div>
					<div
						className={` log-out-div
					${isActive ? 'left-[88%] bg-none' : 'left-[50%] bg-primary'}`}
					>
						<BiLogOutCircle
							className='icon text-[20px] text-white
						transition-all duration-500 ease-in-out'
						/>
					</div>
				</div>
			</div>
		</div>
	);
}

export default Sidebar;
