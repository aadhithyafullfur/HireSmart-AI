export default function Logo() {
  return (
    <div className="flex items-center gap-2">
      <svg
        width="48"
        height="48"
        viewBox="0 0 200 240"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        {/* Document - White background */}
        <rect x="55" y="75" width="90" height="110" rx="8" fill="white" stroke="#1a1a1a" strokeWidth="10"/>
        
        {/* Document text lines - Black */}
        <line x1="70" y1="95" x2="110" y2="95" stroke="#1a1a1a" strokeWidth="3" strokeLinecap="round"/>
        <line x1="70" y1="110" x2="130" y2="110" stroke="#1a1a1a" strokeWidth="3" strokeLinecap="round"/>
        <line x1="70" y1="125" x2="130" y2="125" stroke="#1a1a1a" strokeWidth="3" strokeLinecap="round"/>
        <line x1="70" y1="145" x2="115" y2="145" stroke="#1a1a1a" strokeWidth="3" strokeLinecap="round"/>
        <line x1="70" y1="160" x2="130" y2="160" stroke="#1a1a1a" strokeWidth="3" strokeLinecap="round"/>
        <line x1="70" y1="175" x2="125" y2="175" stroke="#1a1a1a" strokeWidth="3" strokeLinecap="round"/>

        {/* Magnifying glass - Yellow circle with black border */}
        <circle cx="85" cy="75" r="40" fill="none" stroke="#FCD34D" strokeWidth="8"/>
        <circle cx="85" cy="75" r="32" fill="white" stroke="#1a1a1a" strokeWidth="4"/>
        
        {/* User icon inside magnifying glass */}
        <circle cx="85" cy="65" r="6" fill="#FCD34D"/>
        <path d="M 75 80 Q 75 76 85 76 Q 95 76 95 80" fill="#FCD34D"/>

        {/* Magnifying glass handle - Yellow */}
        <g transform="translate(85, 75) rotate(45)">
          <rect x="28" y="-6" width="18" height="12" rx="6" fill="#FCD34D" stroke="#1a1a1a" strokeWidth="2"/>
          <polygon points="46,-6 54,0 46,6" fill="#FCD34D" stroke="#1a1a1a" strokeWidth="2"/>
        </g>

        {/* Document fold/shadow on right */}
        <path d="M 145 75 L 145 90 L 160 75 Z" fill="#e5e5e5" stroke="#1a1a1a" strokeWidth="2"/>

        {/* Folder triangle yellow on left */}
        <polygon points="55,165 40,185 55,185" fill="#FCD34D" stroke="#1a1a1a" strokeWidth="8" strokeLinejoin="round"/>
        
        {/* Folder stick - dark handle */}
        <line x1="40" y1="185" x2="20" y2="205" stroke="#1a1a1a" strokeWidth="10" strokeLinecap="round"/>
      </svg>
      
      <div className="flex items-baseline gap-0">
        <h1 className="text-lg font-black text-yellow-400 bg-black px-2 py-0.5 rounded" style={{letterSpacing: '0.05em'}}>HIRESMART</h1>
        <h1 className="text-lg font-black text-yellow-400 bg-black px-2 py-0.5 rounded" style={{letterSpacing: '0.05em'}}>AI</h1>
      </div>
    </div>
  );
}
