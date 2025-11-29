import React, { useState } from 'react';
import { MOCK_DATA } from './services/dataService';
import OverviewTab from './components/OverviewTab';
import ClientDetailTab from './components/ClientDetailTab';
import { LayoutDashboard, PieChart } from 'lucide-react';

function App() {
  const [activeTab, setActiveTab] = useState<'overview' | 'detail'>('overview');

  return (
    <div className="min-h-screen bg-gray-50 text-gray-900 font-sans pb-12">
      
      {/* Top Navigation Bar */}
      <header className="bg-white border-b border-gray-200 sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16 items-center">
            <div className="flex items-center">
              <div className="bg-blue-600 p-1.5 rounded-lg mr-3">
                <PieChart className="h-6 w-6 text-white" />
              </div>
              <div>
                <h1 className="text-xl font-bold text-gray-900 tracking-tight">O2O <span className="text-blue-600">Vision</span></h1>
                <p className="text-xs text-gray-500 hidden sm:block">Operational Intelligence Dashboard</p>
              </div>
            </div>
            
            <div className="flex items-center space-x-1 bg-gray-100 p-1 rounded-lg">
              <button
                onClick={() => setActiveTab('overview')}
                className={`flex items-center px-4 py-2 rounded-md text-sm font-medium transition-all ${
                  activeTab === 'overview' 
                    ? 'bg-white text-blue-600 shadow-sm' 
                    : 'text-gray-500 hover:text-gray-700'
                }`}
              >
                <LayoutDashboard className="w-4 h-4 mr-2" />
                Team Overview
              </button>
              <button
                onClick={() => setActiveTab('detail')}
                className={`flex items-center px-4 py-2 rounded-md text-sm font-medium transition-all ${
                  activeTab === 'detail' 
                    ? 'bg-white text-blue-600 shadow-sm' 
                    : 'text-gray-500 hover:text-gray-700'
                }`}
              >
                <PieChart className="w-4 h-4 mr-2" />
                Client Detail
              </button>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content Area */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        
        <div className="mb-8">
          <h2 className="text-2xl font-bold text-gray-900">
            {activeTab === 'overview' ? 'Agency Performance Master' : 'Client Profitability Report'}
          </h2>
          <p className="text-gray-500 mt-1">
            {activeTab === 'overview' 
              ? 'Track aggregate ROI, identify churn risks, and monitor total managed GMV.' 
              : 'Deep dive into single client unit economics, LTV, and value creation.'}
          </p>
        </div>

        {activeTab === 'overview' ? (
          <OverviewTab data={MOCK_DATA} />
        ) : (
          <ClientDetailTab data={MOCK_DATA} />
        )}

      </main>
    </div>
  );
}

export default App;
