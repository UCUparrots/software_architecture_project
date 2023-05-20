import React from 'react';
import Link from 'next/link';

function UserList() {
	const items = [
		{ id: 0, name: 'Ilya Konsty', residence: 'Kyiv', phone: '+380283712873' },
		{ id: 1, name: 'Eduard Roller', residence: 'Lviv', phone: '+380871238737' },
		{ id: 2, name: 'Alex Bros', residence: 'Odesa', phone: '+380048014149' },
	];
	return (
		<div>
			<ul>
				{items.map((item) => (
					<Link
						key={item.id}
						href={{
							pathname: '/UserInfoPage',
							query: { id: item.id }, // the data
						}}
					>
						<li
							className='border border-gray rounded-lg w-[40vw] h-[8vh] mb-1 drop-shadow-md
						bg-[#fff] flex justify-around items-center
						hover:border-primary hover:bg-white hover:drop-shadow-xl'
						>
							<div className='text-lg text-primary'>{item.name}</div>
							<div className='text-dark-gray'>
								<div>Phone: {item.phone}</div>
								<div>Residence: {item.residence}</div>{' '}
							</div>
						</li>
					</Link>
				))}
			</ul>
		</div>
	);
}

export default UserList;
