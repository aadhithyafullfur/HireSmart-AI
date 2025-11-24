import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../hooks/useAuth";
import Logo from "./Logo";
export default function Navbar() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const [showMenu, setShowMenu] = useState(false);

  const handleLogout = () => {
    logout();
    navigate("/dashboard");
    setShowMenu(false);
  };

  return (
    <nav className="w-full bg-black border-b border-yellow-500/30 sticky top-0 z-40">
      <div className="max-w-full mx-auto px-4 py-2 flex items-center justify-between">
        {/* Logo - Top Left */}
        <Link to="/dashboard" className="hover:opacity-80 transition flex-shrink-0 min-w-fit">
          <Logo />
        </Link>

        {/* Navigation Links - Center */}
        <div className="hidden md:flex gap-6 items-center flex-1 justify-center">
          <Link
            to="/dashboard"
            className="text-xs text-gray-400 hover:text-white font-medium transition-colors duration-200 relative group whitespace-nowrap"
          >
            Dashboard
            <span className="absolute bottom-0 left-0 w-full h-0.5 bg-yellow-500 scale-x-0 group-hover:scale-x-100 transition-transform duration-300 origin-left"></span>
          </Link>
          <Link
            to="/history"
            className="text-xs text-gray-400 hover:text-white font-medium transition-colors duration-200 relative group whitespace-nowrap"
          >
            History
            <span className="absolute bottom-0 left-0 w-full h-0.5 bg-yellow-500 scale-x-0 group-hover:scale-x-100 transition-transform duration-300 origin-left"></span>
          </Link>
        </div>

        {/* Account Menu - Professional */}
        <div className="relative">
          <button
            onClick={() => setShowMenu(!showMenu)}
            className="relative group flex items-center gap-2 px-4 py-2 rounded-lg bg-black border border-yellow-500/30 hover:border-yellow-500/60 text-white font-medium text-sm transition-all duration-200"
            title={user ? user.name || user.email : "Account"}
          >
            <svg className="w-5 h-5 text-yellow-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <circle cx="12" cy="8" r="4" strokeWidth="1.5"/>
              <path d="M 4 20 Q 4 14 12 14 Q 20 14 20 20" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/>
            </svg>
            <span className="hidden sm:inline text-sm">
              {user ? (user.name?.split(" ")[0] || "Account") : "Account"}
            </span>
            <svg className={`w-4 h-4 text-gray-400 transition-transform duration-300 ${showMenu ? 'rotate-180' : ''}`} fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 14l-7 7m0 0l-7-7m7 7V3" />
            </svg>
          </button>

          {/* Dropdown Menu - Elevated */}
          {showMenu && (
            <div className="absolute right-0 mt-2 w-72 bg-black/95 backdrop-blur-sm rounded-xl shadow-2xl border border-yellow-500/20 z-50 overflow-hidden">
              {user ? (
                <>
                  <div className="px-6 py-4 border-b border-yellow-500/10 bg-gradient-to-r from-yellow-500/5 to-transparent">
                    <p className="text-sm font-semibold text-white">
                      {user.name || "User"}
                    </p>
                    <p className="text-xs text-gray-500 mt-1">{user.email}</p>
                  </div>
                  <div className="p-2 space-y-1">
                    <Link
                      to="/dashboard"
                      onClick={() => setShowMenu(false)}
                      className="flex items-center gap-3 px-4 py-3 text-sm text-gray-300 hover:bg-yellow-500/10 hover:text-yellow-400 rounded-lg transition-colors duration-200"
                    >
                      <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 12l2-3m0 0l7-4 7 4M5 9v10a1 1 0 001 1h12a1 1 0 001-1V9m-9 16l4-4m0 0l4 4m-4-4V5" />
                      </svg>
                      Dashboard
                    </Link>
                    <Link
                      to="/history"
                      onClick={() => setShowMenu(false)}
                      className="flex items-center gap-3 px-4 py-3 text-sm text-gray-300 hover:bg-yellow-500/10 hover:text-yellow-400 rounded-lg transition-colors duration-200"
                    >
                      <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                      </svg>
                      History
                    </Link>
                  </div>
                  <button
                    onClick={handleLogout}
                    className="w-full text-left px-4 py-3 text-sm text-red-400 hover:bg-red-500/10 border-t border-yellow-500/10 transition-colors duration-200 flex items-center gap-3"
                  >
                    <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
                    </svg>
                    Sign Out
                  </button>
                </>
              ) : (
                <>
                  <div className="p-4 space-y-3">
                    <Link
                      to="/login"
                      onClick={() => setShowMenu(false)}
                      className="block w-full px-4 py-2.5 text-sm font-semibold text-black bg-yellow-500 hover:bg-yellow-600 rounded-lg text-center transition-colors duration-200"
                    >
                      Sign In
                    </Link>
                    <Link
                      to="/register"
                      onClick={() => setShowMenu(false)}
                      className="block w-full px-4 py-2.5 text-sm font-semibold text-yellow-400 border border-yellow-500/50 hover:bg-yellow-500/10 rounded-lg text-center transition-colors duration-200"
                    >
                      Create Account
                    </Link>
                  </div>
                </>
              )}
            </div>
          )}
        </div>
      </div>
    </nav>
  );
}
