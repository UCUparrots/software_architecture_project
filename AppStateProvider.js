import { useState, createContext } from 'react';

export const MyContext = createContext();

function AppStateProvider({ children }) {
	const [isActive, setIsActive] = useState(false);
	const [isDoctor, setisDoctor] = useState(true);
	const [isAppointmentOpen, setIsAppointmentOpen] = useState(false);

	const value = {
		isActive,
		setIsActive,
		isDoctor,
		setisDoctor,
		isAppointmentOpen,
		setIsAppointmentOpen,
	};

	return <MyContext.Provider value={value}>{children}</MyContext.Provider>;
}

export default AppStateProvider;
