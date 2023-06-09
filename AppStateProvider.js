import { useState, createContext } from 'react';

export const MyContext = createContext();

function AppStateProvider({ children }) {
	const [isActive, setIsActive] = useState(false);
	const [isDoctor, setIsDoctor] = useState(false);
	const [isAppointmentOpen, setIsAppointmentOpen] = useState(false);
	const [userId, setUserId] = useState('');

	const value = {
		isActive,
		setIsActive,
		isDoctor,
		setIsDoctor,
		isAppointmentOpen,
		setIsAppointmentOpen,
		userId,
		setUserId,
	};

	return <MyContext.Provider value={value}>{children}</MyContext.Provider>;
}

export default AppStateProvider;
